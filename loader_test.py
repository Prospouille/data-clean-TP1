import pytest
import pandas as pd

# This script contains tests for the cleaning functions and should be
# completed by you


@pytest.fixture
def sample_dirty_fname() -> str:
    fname = 'data/sample_dirty.csv'
    return fname


@pytest.fixture
def sample_formatted() -> pd.DataFrame:
    #TODO adr_voie
    df = pd.DataFrame(
        data={'nom': ["Siège Du Ccas (Banque D'Acceuil)",
        'Mibi',
        'Eglise Notre-Dame-Des-Tables',
        'Zoo De Lunaret',
        'Gymnase Jean Bouin',
        pd.NA,
        'Dell'],
        'adr_num': [125,
        pd.NA,
        43,
        50,
        pd.NA,
        pd.NA,
        1],
        'adr_voie': [pd.NA,
        pd.NA,
        "Rue De L'Aiguillerie",
        'Avenue  Agropolis 34000',
        '34Avenue Du Biterrois',
        '1 Place Jacques Mirouse, Montpellier',
        ' Rond-Point Benjamin Franklin'],
        'com_cp': ["34000", pd.NA, "34000", "34090", "34080","34000", pd.NA],
        'com_nom': ['Montpellier',
        pd.NA,
        'Montpellier',
        'Montpellier',
        'Montpellier',
        'Montpellier',
        'Montpellier'],
        'tel1': ['+334 99  52 77 53',
        pd.NA,
        pd.NA,
        '334 67 54 45 20',
        '334 67 75 44 43',
        pd.NA,
        '06 58 57 85 24'],
        'freq_mnt': [pd.NA,
        pd.NA,
        'Tout Les ans',
        'tous les ans',
        'Tous les ans',
        '2019-12-01',
        pd.NA],
        'dermnt': [pd.NaT, pd.NaT, pd.to_datetime('2019-12-01'), pd.to_datetime('2019-04-16'), pd.to_datetime('2019-11-01'), pd.NaT, pd.NaT],
        'lat_coor1': [pd.NA,
        pd.NA,
        3.87957276977398,
        3.87319632529271,
        3.82081921967322,
        3.86982233698134,
        3.91169364237597],
        'long_coor1': [43.6020241317034,
        pd.NA,
        43.6120901983009,
        43.6404472080779,
        43.6327880433471,
        43.6127835439949,
        43.6184228878598]},
        dtype={ "nom" : str, "adr_num" : str, "adr_voie" : str, "com_cp" : str, "com_nom" : str, "tel1" : str, "freq_mnt" : str, "dermnt" : "np.date", "lat_coor1" : "float", "long_coo1" : "float"}
    )

    return df

@pytest.fixture
def sample_sanitized() -> pd.DataFrame:
    # TODO Complete the test case bellow
    df = pd.DataFrame(data={'nom': ["Siège Du Ccas (banque d'acceuil)",
        'Mibi',
        'Eglise Notre-Dame-Des-Tables',
        'Zoo De Lunaret',
        'Gymnase Jean Bouin',
        pd.NA,
        'Dell'],
        'adr_num': [125,
        pd.NA,
        43,
        50,
        pd.NA,
        pd.NA,
        1],
        'adr_voie': [pd.NA,
        pd.NA,
        "Rue De L'Aiguillerie",
        'Avenue Agropolis',
        'Avenue Du Biterrois',
        'Place Jacques Mirouse',
        'Rond-Point Benjamin Franklin'],
        'com_cp': ["34000", pd.NA, "34000", "34090", "34080","34000", pd.NA],
        'com_nom': ['Montpellier',
        pd.NA,
        'Montpellier',
        'Montpellier',
        'Montpellier',
        'Montpellier',
        'Montpellier'],
        'tel1': ['+33 4 99  52 77 53',
        pd.NA,
        pd.NA,
        '+33 4 67 54 45 20',
        '+33 4 67 75 44 43',
        pd.NA,
        '+33 6 58 57 85 24'],
        'freq_mnt': [pd.NA,
        pd.NA,
        'Annuel',
        'Annuel',
        'Annuel',
        pd.NA,
        pd.NA],
        'dermnt': [pd.NaT, pd.NaT, pd.to_datetime('2019-12-01'), pd.to_datetime('2019-04-16'), pd.to_datetime('2019-11-01'), pd.NaT, pd.NaT],
        'lat_coor1': [pd.NA,
        pd.NA,
        3.87957276977398,
        3.87319632529271,
        3.82081921967322,
        3.86982233698134,
        3.91169364237597],
        'long_coor1': [43.6020241317034,
        pd.NA,
        43.6120901983009,
        43.6404472080779,
        43.6327880433471,
        43.6127835439949,
        43.6184228878598]},
        dtype={ "nom" : str, "adr_num" : str, "adr_voie" : str, "com_cp" : str, "com_nom" : str, "tel1" : str, "freq_mnt" : str, "dermnt" : "np.date", "lat_coor1" : "float", "long_coo1" : "float"}
    )
    return df


@pytest.fixture
def sample_framed() -> pd.DataFrame:
    # TODO Complete the test case bellow
    df = pd.DataFrame(
        data={'Intitulé': ["Siège du ccas (banque d'acceuil)",
        'Mibi',
        'Eglise notre-dame-des-tables',
        'Zoo de lunaret',
        'Gymnase jean bouin',
        pd.NA,
        'Dell'],
        'adresse': ["125 , 34000, Montpellier",
        pd.NA,
        "43 Rue De L'Aiguillerie, 34000, Montpellier",
        "50 Avenue Agropolis, 34090, Montpellier",
        "Avenue Du Biterois, 34080, Montpellier",
        "Place Jacques Mirouse, 34000, Montpellier",
        "1 Rond-Point Benjamin Franklin, , Montpellier"],
        'Téléphone': ['+33 4 99  52 77 53',
        pd.NA,
        pd.NA,
        '+33 4 67 54 45 20',
        '+33 4 67 75 44 43',
        pd.NA,
        '+33 6 58 57 85 24'],
        'Fréquence de mainteNAce': [pd.NA,
        pd.NA,
        'Annuel',
        'Annuel',
        'Annuel',
        pd.NA,
        pd.NA],
        'Date de dernière maintenance': [pd.NaT, pd.NaT, pd.to_datetime('2019-12-01'), pd.to_datetime('2019-04-16'), pd.to_datetime('2019-11-01'), pd.NaT, pd.NaT],
        'Latitude': [pd.NA,
        pd.NA,
        3.87957276977398,
        3.87319632529271,
        3.82081921967322,
        3.86982233698134,
        3.91169364237597],
        'Longitude': [43.6020241317034,
        pd.NA,
        43.6120901983009,
        43.6404472080779,
        43.6327880433471,
        43.6127835439949,
        43.6184228878598]},)
    return df


def test_load_formatted_data(sample_dirty_fname, sample_formatted):
    from loader import load_formatted_data
    assert load_formatted_data(sample_dirty_fname).equals(sample_formatted)


def test_sanitize_data(sample_formatted, sample_sanitized):
    from loader import sanitize_data
    assert sanitize_data(sample_formatted).equals(sample_sanitized)


def test_frame_data(sample_sanitized, sample_framed):
    from loader import frame_data
    assert frame_data(sample_sanitized).equals(sample_framed)


def test_load_clean_data(sample_dirty_fname, sample_framed):
    from loader import load_clean_data
    assert load_clean_data(sample_dirty_fname).equals(sample_framed)


def assert_column_equal(clean, target, column):
    # utility function if you which to implement column-specific assertion tests
    assert clean[column].equals(
        target[column]), f"Result should be {clean[column]} but was {target[column]}"
