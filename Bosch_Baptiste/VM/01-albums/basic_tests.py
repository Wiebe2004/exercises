import inspect
import pytest
import album


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(album), reason=f'Skipped because {class_name} has not been defined')


def is_class_abstract(c):
    return inspect.isabstract(c)


def is_abstract_method(cls, method_name):
    return method_name in cls.__abstractmethods__


def has_property(cls, *, property_name, abstract=False):
    if not hasattr(cls, property_name):
        return False
    prop = getattr(cls, property_name)
    if type(prop) is not property:
        return False
    if prop.__isabstractmethod__ != abstract:
        return False
    return True


def has_method(cls, *, method_name, parameter_names=None, abstract=False, static=False):
    if parameter_names is None:
        parameter_names = []

    if not hasattr(cls, method_name):
        return False
    method = getattr(cls, method_name)
    if not inspect.isfunction(method):
        return False
    if abstract:
        if not is_abstract_method(cls, method_name):
            return False
    is_static = isinstance(inspect.getattr_static(cls, method_name), staticmethod)
    if is_static != static:
        return False
    specs = inspect.getfullargspec(method)
    if specs.args != parameter_names:
        return False
    return True

#######
#
# UTIL
#
#######

def test_util_class_is_defined():
    assert 'Util' in dir(album), 'Util class has not been defined'

@if_class_exists('Util')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': 'is_valid_song_id',
        'parameter_names': ['song_id'],
        'abstract': False,
        'static': True,
    },
])
def test_util_methods(kwargs):
    assert has_method(
        album.Util,
        **kwargs), f"Util's method {kwargs['method_name']} is missing or incorrect"

#######
#
# SONG
#
#######

def test_song_class_is_defined():
    assert 'Song' in dir(album), 'Song class has not been defined'


@if_class_exists('Song')
@pytest.mark.parametrize('property_name', [
    'song_id',
])
def test_song_properties(property_name):
    assert has_property(
        album.Song,
        property_name=property_name
        ), f"Song must have property {property_name}"


@if_class_exists('Song')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'song_id', 'title','duration'],
        'abstract': False,
    },
    {
        'method_name': '__str__',
        'parameter_names': ['self'],
        'abstract': False,
    },
])
def test_song_methods(kwargs):
    assert has_method(
        album.Song,
        **kwargs), f"Song's method {kwargs['method_name']} is missing or incorrect"

#######
#
# ALBUM
#
#######

def test_album_class_is_defined():
    assert 'Album' in dir(album), 'Album class has not been defined'


@if_class_exists('Album')
def test_album_class_is_abstract():
    assert is_class_abstract(album.Album)

@if_class_exists('Album')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'used_duration',
        'abstract': False,
    },
    {
        "property_name": 'available_duration',
        'abstract': False,
    },
    {
        "property_name": 'song_titles',
        'abstract': False,
    },
])
def test_album_properties(kwargs):
    assert has_property(album.Album, **kwargs), f"Album's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('Album')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name', 'total_duration'],
        'abstract': False,
    },
    {
        'method_name': 'add_song',
        'parameter_names': ['self','song'],
        'abstract': False,
    },
    {
        'method_name': 'remove_song',
        'parameter_names': ['self','song'],
        'abstract': False,
    },
    {
        'method_name': 'sort_songs_by_duration',
        'parameter_names': ['self'],
        'abstract': False,
    },
    {
        'method_name': 'create_back_cover',
        'parameter_names': ['self'],
        'abstract': True,
    },
])
def test_album_methods(kwargs):
    assert has_method(
        album.Album,
        **kwargs), f"Album's method {kwargs['method_name']} is missing or incorrect"

#######
#
# DIGITALALBUM
#
#######

def test_digitalalbum_class_is_defined():
    assert 'DigitalAlbum' in dir(album), 'DigitalAlbum class has not been defined'


@if_class_exists('DigitalAlbum')
def test_digitalalbum_class_is_not_abstract():
    assert not is_class_abstract(album.DigitalAlbum)


@if_class_exists('DigitalAlbum')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name', 'total_duration','credits'],
        'abstract': False,
    },
    {
        'method_name': 'create_back_cover',
        'parameter_names': ['self'],
        'abstract': False,
    },
])
def test_digitalalbum_methods(kwargs):
    assert has_method(
        album.DigitalAlbum,
        **kwargs), f"DigitalAlbum's method {kwargs['method_name']} is missing or incorrect"

#######
#
# CD
#
#######

def test_cd_class_is_defined():
    assert 'CD' in dir(album), 'CD class has not been defined'


@if_class_exists('CD')
def test_cd_class_is_not_abstract():
    assert not is_class_abstract(album.CD)


@if_class_exists('CD')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name'],
        'abstract': False,
    },
    {
        'method_name': 'create_back_cover',
        'parameter_names': ['self'],
        'abstract': False,
    },
    {
        'method_name': 'add_song',
        'parameter_names': ['self', 'song'],
        'abstract': False,
    },
])
def test_cd_methods(kwargs):
    assert has_method(
        album.CD,
        **kwargs), f"CD's method {kwargs['method_name']} is missing or incorrect"