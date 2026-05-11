<div align="center">
  <img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/header.svg" width="850"/>
  <h1>🚀 Advanced GitHub Metrics Suite</h1>
  <p><i>High-fidelity, theme-aware SVG statistics and animations for your GitHub profile.</i></p>
</div>

---

## ✨ Showcase

This repository contains a collection of premium SVG templates designed to give your GitHub profile a professional, analytical, and high-tech look.

### 📡 Data Visualization
<div align="center">
  <table border="0">
    <tr>
      <td align="center"><b>Activity Trends</b><br/><img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/activity.svg" width="400"/></td>
      <td align="center"><b>Contribution Scanner</b><br/><img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/scanner.svg" width="400"/></td>
    </tr>
    <tr>
      <td align="center"><b>General Stats</b><br/><img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/stats.svg" width="400"/></td>
      <td align="center"><b>Language Analytics</b><br/><img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/languages.svg" width="400"/></td>
    </tr>
  </table>
</div>

### 💻 System & Identity
<div align="center">
  <img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/typing.svg" width="600"/><br/>
  <i>Dynamic typing animation for technical profile highlights.</i>
  <br/><br/>
  <img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/terminal.svg" width="600"/><br/>
  <i>Animated terminal window for role and system information.</i>
</div>

<br/>

<div align="center">
  <img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/focus.svg" width="850"/><br/>
  <i>Modular tactical focus grid for technical competencies.</i>
</div>

### 🌊 Flow & Grid
<div align="center">
  <img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/wave.svg" width="850"/><br/>
  <i>Smooth contribution wave visualization.</i>
</div>
<br/>
<div align="center">
  <img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/matrix.svg" width="850"/><br/>
  <i>Matrix-style contribution grid core.</i>
</div>

---

## 🛠️ Features

- **High Fidelity**: Pure SVG assets with modern CSS animations.
- **Theme Aware**: Automatic switching between Light and Dark modes.
- **Customizable**: Change accent colors and target specific graphs via CLI.
- **Automated**: Built-in GitHub Actions workflow for daily updates.
- **Dedicated Branch**: Metrics are stored in a separate `metrics` branch to keep the main code clean.

---

## 🚀 Getting Started

### 1. Setup Repository
Fork this repository or create a new one using these files.

### 2. Configure Secrets
Go to your repository **Settings > Secrets and variables > Actions** and add:
- `METRICS_TOKEN`: A Personal Access Token (PAT) with `read:user` and `repo` permissions.

### 3. Local Generation
```bash
pip install -r requirements.txt
python generator.py --username YOUR_USERNAME --color "#00FFAA"
```

---

## ⚙️ Customization

You can trigger the **GitHub Metrics Generator** workflow manually to change the appearance of your metrics:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `username` | Your GitHub login | `blackalex1` |
| `color` | Primary accent hex color | `#00FFAA` |
| `graphs` | Specific graphs to build | `all` |

---

<div align="center">
  <a href="https://t.me/blackalex1">
    <img src="https://raw.githubusercontent.com/blackalex1/Statistics/metrics/output/telegram.svg" width="220"/>
  </a>
</div>
