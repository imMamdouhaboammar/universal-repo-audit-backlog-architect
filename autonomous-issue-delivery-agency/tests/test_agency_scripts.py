#!/usr/bin/env python3
"""
Unit tests for Autonomous Issue Delivery Agency validation and snapshot scripts.
"""

import unittest
import subprocess
import tempfile
from pathlib import Path

class TestAgencyScripts(unittest.TestCase):
    def setUp(self):
        self.base_dir = Path(__file__).resolve().parent.parent
        self.scripts_dir = self.base_dir / "scripts"
        self.fixtures_dir = self.base_dir / "tests" / "fixtures"

    def test_validate_contract_success(self):
        contract_path = self.fixtures_dir / "sample_contract.md"
        cmd = [
            "python3",
            str(self.scripts_dir / "validate_delivery_contract.py"),
            "--contract",
            str(contract_path)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(res.returncode, 0, f"Expected valid contract, got: {res.stdout}\n{res.stderr}")
        self.assertIn("is valid", res.stdout)

    def test_validate_receipt_success(self):
        receipt_path = self.fixtures_dir / "sample_receipt.md"
        cmd = [
            "python3",
            str(self.scripts_dir / "validate_delivery_contract.py"),
            "--receipt",
            str(receipt_path)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(res.returncode, 0, f"Expected valid receipt, got: {res.stdout}\n{res.stderr}")
        self.assertIn("is valid", res.stdout)

    def test_validate_contract_missing_sections(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("# Bad Contract\n\nNo objective or scope.\n- [ ] item\nRisk: LOW")
            bad_path = f.name

        try:
            cmd = [
                "python3",
                str(self.scripts_dir / "validate_delivery_contract.py"),
                "--contract",
                bad_path
            ]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("Validation FAILED", res.stdout)
        finally:
            Path(bad_path).unlink()

    def test_validate_contract_secret_detection(self):
        fake_secret = "ghp_" + "a" * 36
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(f"# Contract\n\ntoken = '{fake_secret}'\n")
            bad_path = f.name

        try:
            cmd = [
                "python3",
                str(self.scripts_dir / "validate_delivery_contract.py"),
                "--contract",
                bad_path
            ]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("Potential unredacted secret", res.stdout)
        finally:
            Path(bad_path).unlink()

    def test_run_agency_snapshot(self):
        cmd = [
            "python3",
            str(self.scripts_dir / "run_agency_snapshot.py"),
            str(self.base_dir.parent),
            "--json"
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn('"is_git_repo": true', res.stdout)
        self.assertIn('"branch":', res.stdout)

if __name__ == "__main__":
    unittest.main()
