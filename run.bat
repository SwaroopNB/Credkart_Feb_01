pytest -n=auto --html=Html_Reports\my_edgereport_31_Jan_2026.html --browser edge -k "test_Credkart_Registration_003"
pytest -n=auto --html=Html_Reports\my_firefoxreport_31_Jan_2026.html --browser firefox -k "test_Credkart_Registration_003"
pytest -n=auto --html=Html_Reports\my_chromereport_31_Jan_2026.html --browser chrome -k "test_Credkart_Registration_003"
pytest -n=auto --html=Html_Reports\my_headlessreport_31_Jan_2026.html --browser headless -k "test_Credkart_Registration_003"

pytest -n=auto --html=Html_Reports\my_chromereport_01_feb_2026.html --browser edge 
pause
