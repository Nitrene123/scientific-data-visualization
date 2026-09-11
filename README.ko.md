# 과학 데이터 시각화

[简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

Codex, Claude 및 기타 Agent를 위한 재현 가능한 과학 데이터 시각화 스킬입니다. 실행 가능한 Matplotlib 템플릿 50개, 차트 선택 규칙, 기존 호환 색상 팔레트, PNG/PDF/SVG 출력을 제공합니다.

## 주요 기능

- 비교, 분포, 상관, 차원 축소, 모델 평가, 생존 분석, 오믹스, 시계열, 공간/네트워크, 3D 데이터 지원.
- 3D 막대 행렬, 히트맵 투영, 반응 표면, 3D 산점도, 볼륨, 벡터장 템플릿 포함.
- 기존 프로젝트 팔레트를 기본값으로 유지하고 연속값에 `viridis`, `magma`, `RdBu_r`를 제공합니다.
- 50개의 미리보기 이미지와 PNG, PDF, SVG 출력을 제공합니다.

## 사용 방법

```bash
python scripts/render_template.py --list
python scripts/render_template.py 3d-bar-heat-projection
```

## Codex, Claude 등의 자동 로드

Agent Skills 디렉터리 규칙을 따르며, 설치된 스킬 디렉터리의 최상위에 `SKILL.md`가 있어야 합니다. 설치 후 새 Agent 세션을 시작하면 스킬을 다시 검색합니다. 자동으로 선택되지 않으면 “과학 데이터 시각화 스킬을 사용해 주세요”라고 명시하세요.

### Codex (Windows)

```powershell
git clone https://github.com/Nitrene123/scientific-data-visualization.git
$repo = Join-Path (Get-Location) "scientific-data-visualization"
$codexSkill = Join-Path $env:USERPROFILE ".codex\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $codexSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $codexSkill -Recurse -Force
```

프로젝트 단위 설치는 `.codex/skills/scientific-data-visualization/`를 사용합니다.

### Claude Code (Windows)

```powershell
$claudeSkill = Join-Path $env:USERPROFILE ".claude\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $claudeSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $claudeSkill -Recurse -Force
```

독립적인 Claude Code 프로젝트는 `.claude/skills/scientific-data-visualization/`에 설치하고 Claude Code를 재시작하세요.

## 미리보기

50개의 원본 이미지는 [assets/previews](assets/previews)에 있으며 README의 미리보기 갤러리에서도 확인할 수 있습니다.

## 제한 사항

포함된 데이터는 설명을 위한 결정적 시뮬레이션 데이터입니다. 3D 차트는 세 번째 축에 실제 과학적 의미가 있을 때만 사용하세요.
