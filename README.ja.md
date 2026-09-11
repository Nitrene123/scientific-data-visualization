# 科学データ可視化

[简体中文](README.md) | [繁體中文](README.zh-TW.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

Codex、Claude などの Agent 向けの再現可能な科学データ可視化スキルです。50 個の実行可能な Matplotlib テンプレート、グラフ選択ルール、元の互換カラーパレット、PNG/PDF/SVG 出力を含みます。

## 主な機能

- 比較、分布、相関、次元削減、モデル評価、生存解析、オミクス、時系列、空間/ネットワーク、3D データに対応。
- 3D 柱行列、ヒートマップ投影、応答曲面、3D 散布図、ボリューム、ベクトル場を収録。
- 元のプロジェクト色をデフォルトとして保持し、連続値には `viridis`、`magma`、`RdBu_r` を利用可能。
- 50 枚のプレビュー画像と PNG、PDF、SVG の出力に対応。

## 使い方

```bash
python scripts/render_template.py --list
python scripts/render_template.py 3d-bar-heat-projection
```

## Codex、Claude などへの自動読み込み

Agent Skills のディレクトリ規約に従い、インストール先のスキルディレクトリ直下に `SKILL.md` を置きます。インストール後、新しい Agent セッションを開始してください。自動判定されない場合は「科学データ可視化スキルを使用」と明示します。

### Codex（Windows）

```powershell
git clone https://github.com/Nitrene123/scientific-data-visualization.git
$repo = Join-Path (Get-Location) "scientific-data-visualization"
$codexSkill = Join-Path $env:USERPROFILE ".codex\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $codexSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $codexSkill -Recurse -Force
```

プロジェクト単位では `.codex/skills/scientific-data-visualization/` に配置します。

### Claude Code（Windows）

```powershell
$claudeSkill = Join-Path $env:USERPROFILE ".claude\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $claudeSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $claudeSkill -Recurse -Force
```

プロジェクト単位では `.claude/skills/scientific-data-visualization/` に配置し、Claude Code を再起動します。

## プレビュー

50 枚の画像は [assets/previews](assets/previews) にあり、README のプレビューギャラリーからも確認できます。

## 制限

同梱データは説明用の決定的なシミュレーションデータです。3D 図は第三軸に実際の科学的意味がある場合だけ使用してください。
