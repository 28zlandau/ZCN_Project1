# Zachary Landau, Chloe Lee & Norah Smith
# zlandau@umich.edu, leechloe@umich.edu, norahs@umich.edu
# 9058 8182, 1488 4654, 1084 9048
# AI USE: We used GenAI to help with the function write_results_to_csv (line 152)
# as we had trouble formatting the csv file output.
# We also used GenAI to come up with ideas to use for our function calculations,
# information used in test cases for examples, and general debugging throughout
# the process.
# Uploaded our file with the rubric to ChatGPT to ensure we met the project
# requirements, and realized we had not added edge test cases.
# Functions Created: calc_average_yield_per_crop, calc_average_rainfall_per_region,
# calc_highest_yield_crop_per_region, calc_average_temp_per_region,
# calc_most_frequent_weather_condition_per_region, calc_average_days_to_harvest_per_region

import csv
import unittest

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calc_average_yield_per_crop(data):
    totals = {}
    counts = {}
    for row in data:
        try:
            crop = row['Crop']
            region = row['Region']
            soil = row['Soil_Type']
            value = float(row['Yield_tons_per_hectare'])
        except Exception:
            continue
        key = (crop, region, soil)
        if key not in totals:
            totals[key] = 0.0
            counts[key] = 0
        totals[key] += value
        counts[key] += 1
    averages = {}
    for key in totals:
        averages[key] = totals[key] / counts[key]
    return averages
def calc_average_rainfall_per_region(data):
    totals = {}
    counts = {}
    for row in data:
        try:
            region = row['Region']
            soil = row['Soil_Type']
            irr = row['Irrigation_Used']
            value = float(row['Rainfall_mm'])
        except Exception:
            continue
        key = (region, soil, irr)
        if key not in totals:
            totals[key] = 0.0
            counts[key] = 0
        totals[key] += value
        counts[key] += 1
    averages = {}
    for key in totals:
        averages[key] = totals[key] / counts[key]
    return averages

def calc_highest_yield_crop_per_region(data):
    best = {}
    for row in data:
        try:
            region = row['Region']
            soil = row['Soil_Type']
            weather = row['Weather_Condition']
            crop = row['Crop']
            value = float(row['Yield_tons_per_hectare'])
        except Exception:
            continue
        key = (region, soil, weather)
        if key not in best or value > best[key][1]:
            best[key] = (crop, value)
    results = {}
    for key in best:
        results[key] = best[key][0]
    return results
def calc_average_temp_per_region(data):
    totals = {}
    counts = {}
    for row in data:
        try:
            region = row['Region']
            crop = row['Crop']
            soil = row['Soil_Type']
            value = float(row['Temperature_Celsius'])
        except Exception:
            continue
        key = (region, crop, soil)
        if key not in totals:
            totals[key] = 0.0
            counts[key] = 0
        totals[key] += value
        counts[key] += 1
    averages = {}
    for key in totals:
        averages[key] = totals[key] / counts[key]
    return averages 
 

def calc_most_frequent_weather_condition_per_region(data):
    all_counts = {}
    for row in data:
        region = row.get('Region', '')
        soil = row.get('Soil_Type', '')
        crop = row.get('Crop', '')
        weather = row.get('Weather_Condition', '')
        if not region or not soil or not crop or not weather:
            continue
        key = (region, soil, crop)
        if key not in all_counts:
            all_counts[key] = {}
        if weather not in all_counts[key]:
            all_counts[key][weather] = 0
        all_counts[key][weather] += 1
    results = {}
    for key in all_counts:
        most = None
        most_num = -1
        for condition, count in all_counts[key].items():
            if count > most_num:
                most = condition
                most_num = count
        if most is not None:
            results[key] = most
    return results
def calc_average_days_to_harvest_per_region(data):
    totals = {}
    counts = {}
    for row in data:
        try:
            region = row['Region']
            soil = row['Soil_Type']
            crop = row['Crop']
            value = float(row['Days_to_Harvest'])
        except Exception:
            continue
        key = (region, soil, crop)
        if key not in totals:
            totals[key] = 0.0
            counts[key] = 0
        totals[key] += value
        counts[key] += 1
    averages = {}
    for key in totals:
        averages[key] = totals[key] / counts[key]
    return averages





def write_results_to_csv(results, out_path='results.csv'):
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(["Average Yield per Crop (tons/hectare):"])
        for key, val in sorted(results["average_yield"].items()):
            w.writerow([f"{key}: {val:.3f}"])
        w.writerow([])
        w.writerow(["Highest Yield Crop per Region:"])
        for key, crop in sorted(results["highest_yield"].items()):
            w.writerow([f"{key}: {crop}"])
        w.writerow([])
        w.writerow(["Average Temperature per Region:"])
        for key, val in sorted(results["average_temp"].items()):
            w.writerow([f"{key}: {val:.3f} C"])
        w.writerow([])
        w.writerow(["Most Frequent Weather per Region:"])
        for key, cond in sorted(results["weather"].items()):
            w.writerow([f"{key}: {cond}"])
        w.writerow([])
        w.writerow(["Average Rainfall per Region:"])
        for key, val in sorted(results["average_rain"].items()):
            w.writerow([f"{key}: {val:.3f} mm"])
        w.writerow([])
        w.writerow(["Average Days to Harvest per Region:"])
        if results["average_days_to_harvest"]:
            for key, val in sorted(results["average_days_to_harvest"].items()):
                w.writerow([f"{key}: {val:.3f} days"])
        else:
            w.writerow(["N/A"])
def main():
    data = read_csv('crop_yield.csv')
    results = {
        "average_yield":  calc_average_yield_per_crop(data),
        "highest_yield":  calc_highest_yield_crop_per_region(data),
        "average_temp":   calc_average_temp_per_region(data),
        "weather":        calc_most_frequent_weather_condition_per_region(data),
        "average_rain":   calc_average_rainfall_per_region(data),
        "average_days_to_harvest": calc_average_days_to_harvest_per_region(data),
    }
    write_results_to_csv(results, 'results.csv')
    return results

class TestCropFunctions(unittest.TestCase):
    def setUp(self):
        self.data = read_csv("crop_yield.csv")
    def test_read_csv_is_list(self):
        self.assertIsInstance(self.data, list)
    def test_read_csv_nonempty(self):
        self.assertGreater(len(self.data), 0)
    def test_read_csv_row_is_dict(self):
        self.assertIsInstance(self.data[0], dict)
    def test_read_csv_row_has_keys(self):
        row = self.data[0]
        self.assertIn("Region", row)
        self.assertIn("Crop", row)
        self.assertIn("Soil_Type", row)
        self.assertIn("Yield_tons_per_hectare", row)

    def test_avg_yield_is_dict(self):
        out = calc_average_yield_per_crop(self.data)
        self.assertIsInstance(out, dict)
    def test_avg_yield_nonempty(self):
        out = calc_average_yield_per_crop(self.data)
        self.assertGreaterEqual(len(out), 1)
    def test_avg_yield_key_is_triplet(self):
        out = calc_average_yield_per_crop(self.data)
        k = next(iter(out))
        self.assertIsInstance(k, tuple)
        self.assertEqual(len(k), 3)
    def test_avg_yield_value_is_float(self):
        out = calc_average_yield_per_crop(self.data)
        v = next(iter(out.values()))
        self.assertIsInstance(v, float)


    def test_avg_rain_is_dict(self):
        out = calc_average_rainfall_per_region(self.data)
        self.assertIsInstance(out, dict)
    def test_avg_rain_nonempty(self):
        out = calc_average_rainfall_per_region(self.data)
        self.assertGreaterEqual(len(out), 1)
    def test_avg_rain_key_is_triplet(self):
        out = calc_average_rainfall_per_region(self.data)
        k = next(iter(out))
        self.assertIsInstance(k, tuple)
        self.assertEqual(len(k), 3)
    def test_avg_rain_value_is_float(self):
        out = calc_average_rainfall_per_region(self.data)
        v = next(iter(out.values()))
        self.assertIsInstance(v, float)

    def test_highest_yield_is_dict(self):
        out = calc_highest_yield_crop_per_region(self.data)
        self.assertIsInstance(out, dict)
    def test_highest_yield_nonempty(self):
        out = calc_highest_yield_crop_per_region(self.data)
        self.assertGreaterEqual(len(out), 1)
    def test_highest_yield_key_is_triplet(self):
        out = calc_highest_yield_crop_per_region(self.data)
        k = next(iter(out))
        self.assertIsInstance(k, tuple)
        self.assertEqual(len(k), 3)
    def test_highest_yield_value_is_str(self):
        out = calc_highest_yield_crop_per_region(self.data)
        v = next(iter(out.values()))
        self.assertIsInstance(v, str)
    
    def test_avg_temp_is_dict(self):
        out = calc_average_temp_per_region(self.data)
        self.assertIsInstance(out, dict)
    def test_avg_temp_nonempty(self):
        out = calc_average_temp_per_region(self.data)
        self.assertGreaterEqual(len(out), 1)
    def test_avg_temp_key_is_triplet(self):
        out = calc_average_temp_per_region(self.data)
        k = next(iter(out))
        self.assertIsInstance(k, tuple)
        self.assertEqual(len(k), 3)
    def test_avg_temp_value_is_float(self):
        out = calc_average_temp_per_region(self.data)
        v = next(iter(out.values()))
        self.assertIsInstance(v, float)

    def test_weather_is_dict(self):
        out = calc_most_frequent_weather_condition_per_region(self.data)
        self.assertIsInstance(out, dict)
    def test_weather_nonempty(self):
        out = calc_most_frequent_weather_condition_per_region(self.data)
        self.assertGreaterEqual(len(out), 1)
    def test_weather_key_is_triplet(self):
        out = calc_most_frequent_weather_condition_per_region(self.data)
        k = next(iter(out))
        self.assertIsInstance(k, tuple)
        self.assertEqual(len(k), 3)
    def test_weather_value_is_str(self):
        out = calc_most_frequent_weather_condition_per_region(self.data)
        v = next(iter(out.values()))
        self.assertIsInstance(v, str)

    def test_avg_days_is_dict(self):
        out = calc_average_days_to_harvest_per_region(self.data)
        self.assertIsInstance(out, dict)
    def test_avg_days_nonempty(self):
        out = calc_average_days_to_harvest_per_region(self.data)
        self.assertGreaterEqual(len(out), 1)
    def test_avg_days_key_is_triplet(self):
        out = calc_average_days_to_harvest_per_region(self.data)
        k = next(iter(out))
        self.assertIsInstance(k, tuple)
        self.assertEqual(len(k), 3)
    def test_avg_days_value_is_float(self):
        out = calc_average_days_to_harvest_per_region(self.data)
        v = next(iter(out.values()))
        self.assertIsInstance(v, float)

##EDGE CASES

    def test_avg_yield_single_region_soil(self):
        data = [r for r in self.data if r['Region'] == 'North' and r['Soil_Type'] == 'Clay']
        out = calc_average_yield_per_crop(data)
        self.assertTrue(all(isinstance(k, tuple) and len(k) == 3 for k in out.keys()))
        self.assertTrue(all(isinstance(v, float) for v in out.values()))
    def test_avg_yield_one_key_subset(self):
        first = self.data[0]
        trip = (first['Crop'], first['Region'], first['Soil_Type'])
        subset = [r for r in self.data if (r['Crop'], r['Region'], r['Soil_Type']) == trip]
        out = calc_average_yield_per_crop(subset)
        self.assertEqual(len(out), 1)

    def test_avg_temp_single_region(self):
        data = [r for r in self.data if r['Region'] == 'South']
        out = calc_average_temp_per_region(data)
        self.assertTrue(all(isinstance(k, tuple) and len(k) == 3 for k in out.keys()))
        self.assertTrue(all(isinstance(v, float) for v in out.values()))
    def test_avg_temp_one_key_subset(self):
        first = self.data[0]
        trip = (first['Region'], first['Crop'], first['Soil_Type'])
        subset = [r for r in self.data if (r['Region'], r['Crop'], r['Soil_Type']) == trip]
        out = calc_average_temp_per_region(subset)
        self.assertEqual(len(out), 1)

    def test_highest_yield_single_region_soil(self):
        data = [r for r in self.data if r['Region'] == 'West' and r['Soil_Type'] == 'Clay']
        out = calc_highest_yield_crop_per_region(data)
        self.assertTrue(all(isinstance(k, tuple) and len(k) == 3 for k in out.keys()))
        self.assertTrue(all(isinstance(v, str) for v in out.values()))
    def test_highest_yield_key_present(self):
        first = self.data[0]
        trip = (first['Region'], first['Soil_Type'], first['Weather_Condition'])
        subset = [r for r in self.data if (r['Region'], r['Soil_Type'], r['Weather_Condition']) == trip]
        out = calc_highest_yield_crop_per_region(subset)
        self.assertIn(trip, out)



    def test_weather_single_region(self):
        data = [r for r in self.data if r['Region'] == 'North']
        out = calc_most_frequent_weather_condition_per_region(data)
        self.assertTrue(all(isinstance(k, tuple) and len(k) == 3 for k in out.keys()))
        self.assertTrue(all(isinstance(v, str) for v in out.values()))
    def test_weather_one_key_subset(self):
        first = self.data[0]
        trip = (first['Region'], first['Soil_Type'], first['Crop'])
        subset = [r for r in self.data if (r['Region'], r['Soil_Type'], r['Crop']) == trip]
        out = calc_most_frequent_weather_condition_per_region(subset)
        self.assertIn(trip, out)
 
 
    def test_avg_days_single_region_soil(self):
        data = [r for r in self.data if r['Region'] == 'East' and r['Soil_Type'] == 'Sandy']
        out = calc_average_days_to_harvest_per_region(data)
        self.assertTrue(all(isinstance(k, tuple) and len(k) == 3 for k in out.keys()))
        self.assertTrue(all(isinstance(v, float) for v in out.values()))
    def test_avg_days_one_key_subset(self):
        first = self.data[0]
        trip = (first['Region'], first['Soil_Type'], first['Crop'])
        subset = [r for r in self.data if (r['Region'], r['Soil_Type'], r['Crop']) == trip]
        out = calc_average_days_to_harvest_per_region(subset)
        self.assertEqual(len(out), 1)



    def test_main_is_dict(self):
        result = main()
        self.assertIsInstance(result, dict)
    def test_main_has_all_keys(self):
        result = main()
        self.assertIn("average_yield", result)
        self.assertIn("highest_yield", result)
        self.assertIn("average_temp", result)
        self.assertIn("weather", result)
        self.assertIn("average_rain", result)
        self.assertIn("average_days_to_harvest", result)
    def test_main_values_are_dicts(self):
        result = main()
        self.assertIsInstance(result["average_yield"], dict)
        self.assertIsInstance(result["highest_yield"], dict)
        self.assertIsInstance(result["average_temp"], dict)
        self.assertIsInstance(result["weather"], dict)
        self.assertIsInstance(result["average_rain"], dict)
        self.assertIsInstance(result["average_days_to_harvest"], dict)
    def test_main_sections_nonempty(self):
        result = main()
        self.assertGreaterEqual(len(result["average_yield"]), 1)
        self.assertGreaterEqual(len(result["highest_yield"]), 1)
        self.assertGreaterEqual(len(result["average_temp"]), 1)
        self.assertGreaterEqual(len(result["weather"]), 1)
        self.assertGreaterEqual(len(result["average_rain"]), 1)
        self.assertGreaterEqual(len(result["average_days_to_harvest"]), 1)

if __name__ == "__main__":
    unittest.main()
 





