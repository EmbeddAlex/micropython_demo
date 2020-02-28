def web_page(bme):
    return """<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="10">
  <link rel="icon" href="data:,"><style>body { text-align: center; font-family: "Trebuchet MS", Arial;}
  table { border-collapse: collapse; width:35%; margin-left:auto; margin-right:auto; }
  th { padding: 12px; background-color: #37bcd0; color: white; }
  tr { border: 1px solid #ddd; padding: 12px; }
  tr:hover { background-color: #bcbcbc; }
  td { border: none; padding: 12px; }
  .sensor { color:white; font-weight: bold; background-color: #bcbcbc; padding: 1px;
  </style></head><body><h1>IoT with MicroPython</h1>
  <table><tr><th>MEASUREMENT</th><th>VALUE</th></tr>
  <tr><td>Temp. Celsius</td><td><span class="sensor">""" + str(bme.temperature) + """</span></td></tr>
  <tr><td>Temp. Fahrenheit</td><td><span class="sensor">""" + str(
        round((bme.read_temperature() / 100.0) * (9 / 5) + 32, 2)) + """F</span></td></tr>
  <tr><td>Pressure</td><td><span class="sensor">""" + str(bme.pressure) + """</span></td></tr>
  <tr><td>Pressure. Millimeters mercury</td><td><span class="sensor">""" + str(bme.pressure_hg) + """mmHg</span></td></tr>
  <tr><td>Humidity</td><td><span class="sensor">""" + str(bme.humidity) + """</span></td></tr></body></html>"""
