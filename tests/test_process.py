from medical_reports.process import clean_data

def test_clean():
    assert clean_data("abc") == "ABC"
