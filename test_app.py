import chromedriver_autoinstaller
chromedriver_autoinstaller.install() # This automatically downloads the right driver for your Chrome version

from app import app # Imports dash app

# test 1: check for header
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    # wait for H1 to appear on the page timeout after 10s
    dash_duo.wait_for_element("h1", timeout=10)

# Test 2: chwck for visuals
def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

# Test 3: check for where u choose a region
def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-radio", timeout=10)