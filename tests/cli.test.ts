import { describe, expect, test } from 'bun:test';
import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const ROOT_DIR = resolve(__dirname, '..');

describe('Universal Autonomous Engineering Suite CLI & Manifests', () => {
  test('package.json exists and contains valid metadata', () => {
    const pkgPath = join(ROOT_DIR, 'package.json');
    expect(existsSync(pkgPath)).toBe(true);
    const pkg = JSON.parse(readFileSync(pkgPath, 'utf8'));
    expect(pkg.name).toBe('universal-repo-audit-backlog-architect');
    expect(pkg.bin).toBeDefined();
    expect(pkg.bin['universal-repo-audit-backlog-architect']).toBe('./bin/cli.js');
    expect(pkg.keywords).toContain('agent-skill');
    expect(pkg.keywords).toContain('omni-skill');
  });

  test('marketplace.json exists and conforms to Claude plugin format', () => {
    const marketPath = join(ROOT_DIR, 'marketplace.json');
    expect(existsSync(marketPath)).toBe(true);
    const market = JSON.parse(readFileSync(marketPath, 'utf8'));
    expect(market.name).toBe('universal-repo-audit-backlog-architect');
    expect(market.entrypoint).toBe('SKILL.md');
    expect(market.compatibility).toBeDefined();
    expect(market.compatibility.claudeCode).toBeDefined();
  });

  test('.skills.json exists and conforms to Skills.sh registry format', () => {
    const skillsPath = join(ROOT_DIR, '.skills.json');
    expect(existsSync(skillsPath)).toBe(true);
    const skills = JSON.parse(readFileSync(skillsPath, 'utf8'));
    expect(skills.name).toBe('universal-repo-audit-backlog-architect');
    expect(skills.skill).toBe('SKILL.md');
    expect(skills.tags).toContain('agent-skill');
  });

  test('root SKILL.md exists and has valid YAML frontmatter', () => {
    const skillPath = join(ROOT_DIR, 'SKILL.md');
    expect(existsSync(skillPath)).toBe(true);
    const content = readFileSync(skillPath, 'utf8');
    expect(content.startsWith('---')).toBe(true);
    expect(content).toContain('name: universal-repo-audit-backlog-architect');
    expect(content).toContain('description:');
  });

  test('bin/cli.js outputs help and info correctly', () => {
    const cliPath = join(ROOT_DIR, 'bin', 'cli.js');
    expect(existsSync(cliPath)).toBe(true);

    const helpRes = spawnSync('bun', [cliPath, '--help'], { encoding: 'utf8' });
    expect(helpRes.status).toBe(0);
    expect(helpRes.stdout).toContain('Universal Autonomous Engineering Suite');
    expect(helpRes.stdout).toContain('Usage:');

    const infoRes = spawnSync('bun', [cliPath, 'info'], { encoding: 'utf8' });
    expect(infoRes.status).toBe(0);
    expect(infoRes.stdout).toContain('Universal Repo Audit & Autonomous Delivery Agency Suite');
    expect(infoRes.stdout).toContain('1. Universal Repository Audit & Backlog Architect');
    expect(infoRes.stdout).toContain('2. Autonomous Issue Delivery Agency');
  });
});
