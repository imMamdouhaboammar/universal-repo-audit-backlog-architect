#!/usr/bin/env node

/**
 * Universal Repo Audit & Autonomous Delivery Agency CLI Runner
 * Compatible with Bun and Node.js (>= 18.0.0)
 * 
 * Part of the Autonomous Engineering Suite by Mamdouh Aboammar
 */

import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT_DIR = resolve(__dirname, '..');

const pkgPath = join(ROOT_DIR, 'package.json');
let version = '1.0.0';
try {
  if (existsSync(pkgPath)) {
    const pkg = JSON.parse(readFileSync(pkgPath, 'utf8'));
    version = pkg.version || version;
  }
} catch {
  // fallback to default
}

function printUsage() {
  console.log(`
Universal Autonomous Engineering Suite (v${version})
Audit, Backlog Architecture & Autonomous Issue-to-Merge Delivery

Usage:
  universal-repo-audit-backlog-architect <command> [options]

Commands:
  audit [path]               Run 14-domain safe repository snapshot & inspection
  validate-backlog <file>    Validate issue format, checkboxes, and dependency DAG
  agency-snapshot [path]     Run autonomous delivery agency repository snapshot
  validate-contract <args>   Validate delivery contract or closure receipt markdown
  test                       Run suite test runners (Bun and Python unittests)
  install                    Run universal installer across AI agent environments
  info                       Show suite capabilities, modules, and host compatibility
  help, --help, -h           Show this help message

Aliases:
  repo-audit <command>
  delivery-agency <command>

Examples:
  npx universal-repo-audit-backlog-architect audit .
  npx universal-repo-audit-backlog-architect validate-backlog ./tests/fixtures/sample_issue.md
  bun run validate:contract -- --contract ./autonomous-issue-delivery-agency/tests/fixtures/sample_contract.md
`);
}

function printInfo() {
  console.log(`
================================================================================
  Universal Repo Audit & Autonomous Delivery Agency Suite (v${version})
  Author: Mamdouh Aboammar <https://github.com/imMamdouhaboammar>
  Omni-Skill: 100% Portable Across Agent Ecosystems
================================================================================

Modules:
  1. Universal Repository Audit & Backlog Architect
     - 16-Phase audit lifecycle from git baseline to acyclic dependency DAG
     - 14 Engineering inspection domains (Correctness, Security, Perf, etc.)
     - Single-session vertical tracer slicing with binary acceptance criteria

  2. Autonomous Issue Delivery Agency
     - 20-Phase autonomous issue-to-merge engineering lifecycle
     - Single active issue rule & single write owner discipline
     - TDD verification, atomic commits, independent review, CI verification
     - Authorized merge, post-merge health checks, and delivery receipts

Compatibility:
  ✓ Claude Code & Claude Desktop (marketplace.json & SKILL.md)
  ✓ Skills.sh Registry (.skills.json)
  ✓ OpenAI Codex & OpenCode (.codex-plugin/plugin.json)
  ✓ ChatGPT Custom GPTs (submission/chatgpt-instructions.md)
  ✓ Antigravity & Gemini CLI (Universal Agent Skills)
  ✓ Cursor & Windsurf (.cursor/skills)
  ✓ Bun & Node.js Zero-Install CLI (npx/bunx)
`);
}

function runScript(scriptPath, args) {
  const fullPath = join(ROOT_DIR, scriptPath);
  if (!existsSync(fullPath)) {
    console.error(`Error: Script not found at ${fullPath}`);
    process.exit(1);
  }

  const result = spawnSync('python3', [fullPath, ...args], {
    stdio: 'inherit',
    cwd: process.cwd()
  });

  process.exit(result.status ?? 0);
}

function runInstall() {
  const installPath = join(ROOT_DIR, 'install.sh');
  if (!existsSync(installPath)) {
    console.error(`Error: install.sh not found at ${installPath}`);
    process.exit(1);
  }

  const result = spawnSync('bash', [installPath], {
    stdio: 'inherit',
    cwd: ROOT_DIR
  });

  process.exit(result.status ?? 0);
}

function runTests() {
  console.log('Running test suites...');
  
  // 1. Python unittests for Module 2
  const pyResult = spawnSync('python3', ['-m', 'unittest', 'discover', '-s', join(ROOT_DIR, 'autonomous-issue-delivery-agency/tests'), '-p', 'test_*.py'], {
    stdio: 'inherit',
    cwd: ROOT_DIR
  });

  if (pyResult.status !== 0) {
    process.exit(pyResult.status ?? 1);
  }

  console.log('All tests passed successfully!');
}

function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  if (!command || command === 'help' || command === '--help' || command === '-h') {
    printUsage();
    process.exit(0);
  }

  switch (command) {
    case 'info':
    case '--info':
      printInfo();
      break;

    case 'audit':
      runScript('universal-repo-audit-backlog-architect/scripts/extract_repo_snapshot.py', args.slice(1));
      break;

    case 'validate-backlog':
      runScript('universal-repo-audit-backlog-architect/scripts/validate_backlog.py', args.slice(1));
      break;

    case 'agency-snapshot':
      runScript('autonomous-issue-delivery-agency/scripts/run_agency_snapshot.py', args.slice(1));
      break;

    case 'validate-contract':
      runScript('autonomous-issue-delivery-agency/scripts/validate_delivery_contract.py', args.slice(1));
      break;

    case 'test':
      runTests();
      break;

    case 'install':
      runInstall();
      break;

    default:
      console.error(`Unknown command: ${command}\n`);
      printUsage();
      process.exit(1);
  }
}

main();
