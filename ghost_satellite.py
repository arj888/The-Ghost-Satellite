import os
import sys
import subprocess
import requests
from skyfield.api import load

def run_defense_core():
    print("=== THE GHOST SATELLITE: INTEGRATED DEFENSE CORE ACTIVATED ===")
    
    # Check and install google-colab-ai if missing inside the module
    try:
        from google.colab import ai
    except ImportError:
        print("[System Info]: Setting up AI communication bridge...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "google-colab-ai", "-q"])
        from google.colab import ai

    # 1. Fetching Live Multi-Satellite Data
    tle_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=visual&FORMAT=tle"
    response = requests.get(tle_url)
    tle_data = response.text.splitlines()

    ts = load.timescale()
    t = ts.now()

    # 2. Target Defense Zone (India Bounding Box)
    INDIA_MIN_LAT, INDIA_MAX_LAT = 8.4, 37.6
    INDIA_MIN_LON, INDIA_MAX_LON = 68.7, 97.2

    # 3. Whitelist Database
    SAFE_REGISTRY = ["GSAT-31", "INSAT-3DR", "CARTOSAT-2"]
    breached_satellites = []

    for i in range(0, len(tle_data) - 2, 3):
        name = tle_data[i].strip()
        line1 = tle_data[i+1]
        line2 = tle_data[i+2]
        
        try:
            from skyfield.sgp4lib import EarthSatellite
            sat = EarthSatellite(line1, line2, name, ts)
            geocentric = sat.at(t)
            subpoint = geocentric.subpoint()
            
            lat = subpoint.latitude.degrees
            lon = subpoint.longitude.degrees
            alt = subpoint.elevation.km
            
            if (INDIA_MIN_LAT <= lat <= INDIA_MAX_LAT) and (INDIA_MIN_LON <= lon <= INDIA_MAX_LON):
                if name not in SAFE_REGISTRY:
                    breached_satellites.append({"name": name, "lat": lat, "lon": lon, "alt": alt})
        except:
            continue

    print(f"Airspace Scan Complete. Unverified Objects Detected: {len(breached_satellites)}")

    if breached_satellites:
        target = breached_satellites[0]
        print(f"\n[🚨 CRITICAL ALERT] UNVERIFIED OBJECT BREACHED REGIONAL AIRSPACE!")
        print(f"Target Name: {target['name']} | Lat: {target['lat']:.4f} | Lon: {target['lon']:.4f} | Alt: {target['alt']:.2f} km")
        print("Initiating Gemini AI Strategic Threat Profiling...")
        
        ai_prompt = f"""
        You are the core AI of a national aerospace defense system 'The Ghost Satellite'.
        An unverified satellite has breached regional airspace coordinates.
        - Object Name: {target['name']}
        - Telemetry: Lat {target['lat']:.4f}, Lon {target['lon']:.4f}, Altitude {target['alt']:.2f} km
        - Database Status: UNKNOWN / NO GOVERNMENT RECORD FOUND

        Act as a Senior Military Intelligence Officer. Provide a professional, strictly formal threat assessment in pure English:
        1. Spy/Reconnaissance Probability: Estimate percentage based on LEO orbit and missing registry data.
        2. Tactical Implications: Outline potential risks (Surveillance, Electronic Espionage, SIGINT).
        No conversational fillers. Pure tactical data.
        """
        
        try:
            ai_response = ai.generate_text(ai_prompt)
            print("\n=== AI INTEL REPORT ===")
            print(ai_response)
            print("=======================")
        except Exception as e:
            print(f"\n[AI Connection Note]: Active threat logged. AI Bridge active but response delayed.")
    else:
        print("\n[🟢 SYSTEM SAFE] No unverified satellite breaches detected in the target sector.")
    print("=============================================================")
