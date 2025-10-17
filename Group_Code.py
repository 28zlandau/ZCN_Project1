#Zachary Landau, Chloe Lee & Norah Smith 
import csv
import unittest

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

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
 





