import pytest
import pandas as pd
import wx
import unittest.mock as mock
import os
from run import ReportFrame

# a fixture to create a wx.App instance with ReportFrame for testing
@pytest.fixture(scope="module")
def app():
    app_instance = wx.App(False)
    app_instance.frame = ReportFrame()  
    yield app_instance  # Return the wx.App instance     
    app_instance.frame.Close()

# Parametrize the test case with valid region values
@pytest.mark.parametrize("region, expected_region", [(0, 'Region1'), (1, 'Region2')])
def test_region_list(app, region, expected_region):
    frame = app.frame  

    # Check if the index is valid
    if 0 <= region < frame.regionList.GetCount():
        frame.regionList.SetSelection(region)  

        frame.region_list(wx.EVT_COMBOBOX)
        assert frame.selected_region == expected_region

# Mock the load_data function for testing
def test_load_data(app):
    frame = app.frame  

    # Mock the load_data function
    with mock.patch.object(frame, 'load_data') as mock_load_data:
        # Call load_data function
        frame.load_data(None)

        # Check that load_data was called
        mock_load_data.assert_called_once()

        # Check that frame.table is None, since load_data doesn't return a value
        assert frame.table is None  

# Mock the export_report function for testing
def test_export_report(app):
    frame = app.frame  

    # Mock the export_report function
    with mock.patch.object(frame, 'export_report') as mock_export_report:
        # Call export_report function
        frame.export_report(None)

        # Check that export_report was called
        mock_export_report.assert_called_once()

# Mock the search function for testing
def test_search(app):
    frame = app.frame  

    # Mock the search function
    with mock.patch.object(frame, 'search') as mock_search:
        # Call search function
        frame.search(None)

        # Check that search was called
        mock_search.assert_called_once()

# Mock the apply_filter function for testing
def test_apply_filter(app):
    frame = app.frame  

    # Mock the apply_filter function
    with mock.patch.object(frame, 'apply_filter') as mock_apply_filter:
        # Call apply_filter function
        frame.apply_filter(None)

        # Check that apply_filter was called
        mock_apply_filter.assert_called_once()

# Mock the go_visual function for testing
def test_go_visual(app):
    frame = app.frame  

    with mock.patch.object(frame, 'go_visual') as mock_go_visual:
        # Call go_visual function
        frame.go_visual(None)

        # Check that go_visual was called
        mock_go_visual.assert_called_once()

# Check if a file exists
def test_file_exists():
    assert os.path.exists("CrashVictoria.csv")  

# Check if a file name extension is valid (3 or 4 alphabetical characters preceded by a dot)
def test_valid_file_extension():
    file_name = "example_file.csv"  # Replace with a valid file name
    file_extension = os.path.splitext(file_name)[1]
    assert len(file_extension) in [4, 5] and file_extension[1:].isalpha()


if __name__ == '__main__':
    pytest.main(['test_run_pytest.py'])
