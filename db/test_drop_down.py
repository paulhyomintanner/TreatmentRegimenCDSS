import unittest
from unittest.mock import patch
from tkinter import messagebox

from drop_down import TreatmentApp

class TestTreatmentApp(unittest.TestCase):
    def setUp(self):
        self.app = TreatmentApp(None)

    def test_filter_by_disease(self):
        treatments = [
            {"disease": "A", "eligibility": []},
            {"disease": "B", "eligibility": []},
            {"disease": "A", "eligibility": []},
        ]
        filtered_treatments = self.app.filter_by_disease(treatments, "A")
        self.assertEqual(len(filtered_treatments), 2)
        self.assertEqual(filtered_treatments[0]["disease"], "A")
        self.assertEqual(filtered_treatments[1]["disease"], "A")

    def test_filter_by_severity(self):
        treatments = [
            {"eligibility": [{"severity": "Mild"}, {"severity": "Moderate"}]},
            {"eligibility": [{"severity": "Severe"}]},
            {"eligibility": [{"severity": "Mild"}]},
        ]
        filtered_treatments = self.app.filter_by_severity(treatments, "Mild")
        self.assertEqual(len(filtered_treatments), 2)
        self.assertEqual(filtered_treatments[0]["eligibility"][0]["severity"], "Mild")
        self.assertEqual(filtered_treatments[1]["eligibility"][0]["severity"], "Mild")

    def test_filter_by_exclusions(self):
        treatments = [
            {"eligibility": [{"exclusion": ["A", "B"]}]},
            {"eligibility": [{"exclusion": ["C"]}]},
            {"eligibility": [{"exclusion": ["B", "D"]}]},
        ]
        filtered_treatments = self.app.filter_by_exclusions(treatments, ["B", "C"])
        self.assertEqual(len(filtered_treatments), 1)
        self.assertEqual(filtered_treatments[0]["eligibility"][0]["exclusion"], ["A", "B"])

    def test_filter_patient_profile(self):
        treatments = [
            {"eligibility": [{"patient_profile": {"age_range": {"min": 20, "max": 30}, "min_weight": 50}}]},
            {"eligibility": [{"patient_profile": {"age_range": {"min": 30, "max": 40}, "min_weight": 60}}]},
            {"eligibility": [{"patient_profile": {"age_range": {"min": 40, "max": 50}, "min_weight": 70}}]},
        ]
        filtered_treatments = self.app.filter_patient_profile(treatments, 25, 55)
        self.assertEqual(len(filtered_treatments), 1)
        self.assertEqual(filtered_treatments[0]["eligibility"][0]["patient_profile"]["age_range"]["min"], 20)
        self.assertEqual(filtered_treatments[0]["eligibility"][0]["patient_profile"]["min_weight"], 50)

    @patch("drop_down.ctk.CTkLabel")
    def test_submit_page_one(self, mock_ctk_label):
        self.app.weight_entry = "70"
        self.app.height_entry = "170"
        self.app.age_entry = "25"
        self.app.cpg_dropdown = "CPG1"
        self.app.exclusion_checkboxes = {"A": 1, "B": 0, "C": 1}
        self.app.submit_page_one()
        self.assertEqual(self.app.user_data["weight"], 70)
        self.assertEqual(self.app.user_data["height"], 170)
        self.assertEqual(self.app.user_data["age"], 25)
        self.assertEqual(self.app.user_data["cpg"], "CPG1")
        self.assertEqual(self.app.user_data["exclusions"], ["A", "C"])
        mock_ctk_label.assert_not_called()

    @patch("drop_down.ctk.CTkLabel")
    def test_submit_page_two(self, mock_ctk_label):
        self.app.disease_dropdown = "Disease1"
        self.app.severity_dropdown = "Mild"
        self.app.user_data["diseases"] = []
        self.app.submit_page_two()
        self.assertEqual(len(self.app.user_data["diseases"]), 1)
        self.assertEqual(self.app.user_data["diseases"][0]["disease"], "Disease1")
        self.assertEqual(self.app.user_data["diseases"][0]["severity"], "Mild")
        mock_ctk_label.assert_not_called()

    @patch("drop_down.messagebox.showerror")
    def test_retrieve_treatments_missing_inputs(self, mock_showerror):
        self.app.user_data = {}
        self.app.retrieve_treatments()
        mock_showerror.assert_called_once_with("Error", "Please fill in all the necessary inputs before retrieving treatments.")

if __name__ == "__main__":
    unittest.main()