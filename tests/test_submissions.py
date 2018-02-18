from pathlib import Path as P
import json
from jsonschema import validate
import os
import pytest


schema_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data/museval.schema.json',
)

with open(schema_path) as schema_file:
    schema = json.load(schema_file)


track_list_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data/mus18_test_tracks.json',
)

with open(track_list_path) as tracks_file:
    track_list = json.load(tracks_file)


def submissions():
    p = P('submissions')
    for submission_dir in p.iterdir():
        if submission_dir.is_dir():
            yield submission_dir, json_tracks(submission_dir)


def json_tracks(x):
    p = P(x)
    if p.exists():
        json_paths = p.glob('**/*.json')
        for json_path in json_paths:
            yield json_path


def check_equal(L1, L2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)


@pytest.fixture(
    params=[(k, v) for k, l in submissions() for v in l],
    ids=['%s-%s' % (k.stem, v.stem) for k, l in submissions() for v in l]
)
def submission_tracks(request):
    return request.param


@pytest.fixture(
    params=submissions(),
    ids=['%s' % k.stem for k, l in submissions()]
)
def submission(request):
    return request.param[0]


@pytest.fixture
def track(submission_tracks):
    return submission_tracks[1]


def test_submission(submission):
    # verify that submission name is short than 4 characters
    assert len(submission.stem) <= 4
    tracks = list(json_tracks(submission))
    # verify that all tracks were submitted
    assert len(list(tracks)) == len(track_list)
    assert check_equal([track.stem for track in tracks], track_list)
    # check if description.md does exist
    assert P(submission / 'description.md').exists()


def test_scores(track):
    with open(track) as json_file:
        json_string = json.loads(json_file.read())
        validate(json_string, schema)
