<div align="center">
  <table>
    <tr>
      <td width="180">
        <!-- 头像：圆形裁剪 -->
        <img src="https://github.com/wzxgA.png" width="160" height="160" style="border-radius: 50%; border: 3px solid #e94560; box-shadow: 0 0 20px rgba(233,69,96,0.3);" />
      </td>
      <td>
        <!-- 动态文字：Hi, I'm wzxgA 打字机动画 + 渐变色 -->
        <svg width="520" height="120" viewBox="0 0 520 120">
          <defs>
            <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#ff6b9d">
                <animate attributeName="stop-color" values="#ff6b9d;#c471ed;#12c2e9;#ff6b9d" dur="5s" repeatCount="indefinite"/>
              </stop>
              <stop offset="50%" stop-color="#c471ed">
                <animate attributeName="stop-color" values="#c471ed;#12c2e9;#f64f59;#c471ed" dur="5s" repeatCount="indefinite"/>
              </stop>
              <stop offset="100%" stop-color="#12c2e9">
                <animate attributeName="stop-color" values="#12c2e9;#f64f59;#ff6b9d;#12c2e9" dur="5s" repeatCount="indefinite"/>
              </stop>
            </linearGradient>
          </defs>

          <!-- 第一行 Hi, -->
          <text x="20" y="52" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="42" font-weight="700" fill="url(#textGrad)">
            <animate attributeName="opacity" values="0;1" dur="0.6s" begin="0s" fill="freeze" />
            Hi,
          </text>

          <!-- 第二行 I'm wzxgA  打字机效果（逐字出现） -->
          <g>
            <text x="20" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              I
              <animate attributeName="opacity" values="0;0;1;1" dur="3.2s" begin="0.5s" repeatCount="indefinite" />
            </text>
            <text x="50" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              '
              <animate attributeName="opacity" values="0;0;1;1" dur="3.0s" begin="0.65s" repeatCount="indefinite" />
            </text>
            <text x="62" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              m
              <animate attributeName="opacity" values="0;0;1;1" dur="2.8s" begin="0.8s" repeatCount="indefinite" />
            </text>
            <text x="98" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              w
              <animate attributeName="opacity" values="0;0;1;1" dur="2.6s" begin="1.0s" repeatCount="indefinite" />
            </text>
            <text x="138" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              z
              <animate attributeName="opacity" values="0;0;1;1" dur="2.4s" begin="1.2s" repeatCount="indefinite" />
            </text>
            <text x="176" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              x
              <animate attributeName="opacity" values="0;0;1;1" dur="2.2s" begin="1.4s" repeatCount="indefinite" />
            </text>
            <text x="214" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              g
              <animate attributeName="opacity" values="0;0;1;1" dur="2.0s" begin="1.6s" repeatCount="indefinite" />
            </text>
            <text x="254" y="100" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="48" font-weight="800" fill="url(#textGrad)">
              A
              <animate attributeName="opacity" values="0;0;1;1" dur="1.8s" begin="1.8s" repeatCount="indefinite" />
            </text>

            <!-- 光标 -->
            <rect x="295" y="60" width="4" height="46" rx="2" fill="#e94560">
              <animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite" />
            </rect>

            <!-- 手型摆动图标 -->
            <text x="440" y="100" font-size="44">
              👋
              <animateTransform attributeName="transform" type="rotate" values="0 460 90;-10 460 90;10 460 90;-5 460 90;0 460 90" dur="1.5s" repeatCount="indefinite" />
            </text>
          </g>
        </svg>
      </td>
    </tr>
  </table>
</div>

<br/>

---

## 📊 GitHub Stats

<!-- 纯手绘 SVG 统计表，复刻参考图风格，不调用任何第三方接口 -->
<div align="center">
<svg width="760" height="280" viewBox="0 0 760 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.25"/>
    </filter>
    <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c471ed"/>
      <stop offset="50%" stop-color="#e94560"/>
      <stop offset="100%" stop-color="#ff6b9d"/>
    </linearGradient>
  </defs>

  <!-- 卡片背景 -->
  <rect x="10" y="10" width="740" height="260" rx="12" fill="#21222c" stroke="#3a3c4e" stroke-width="1.5" filter="url(#cardShadow)"/>

  <!-- 标题 -->
  <text x="40" y="55" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="24" font-weight="700" fill="#e94560">
    wzxgA's GitHub Stats
  </text>

  <!-- 分隔线 -->
  <line x1="40" y1="75" x2="480" y2="75" stroke="#3a3c4e" stroke-width="1"/>

  <!-- 统计项 1: Total Stars Earned -->
  <g>
    <circle cx="55" cy="105" r="9" fill="#ffd166" opacity="0.15"/>
    <text x="48" y="112" font-size="18">⭐</text>
    <text x="85" y="112" font-family="'Segoe UI', sans-serif" font-size="17" fill="#e4e4e7" font-weight="500">Total Stars Earned:</text>
    <text x="420" y="112" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#f0f0f0" text-anchor="middle">
      773
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.5s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- 统计项 2: Total Commits -->
  <g>
    <circle cx="55" cy="145" r="9" fill="#7fffd4" opacity="0.15"/>
    <text x="48" y="152" font-size="18">⏱</text>
    <text x="85" y="152" font-family="'Segoe UI', sans-serif" font-size="17" fill="#e4e4e7" font-weight="500">Total Commits (2026):</text>
    <text x="420" y="152" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#f0f0f0" text-anchor="middle">
      669
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.3s" begin="0.2s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- 统计项 3: Total PRs -->
  <g>
    <circle cx="55" cy="185" r="9" fill="#60a5fa" opacity="0.15"/>
    <text x="48" y="192" font-size="18">🔀</text>
    <text x="85" y="192" font-family="'Segoe UI', sans-serif" font-size="17" fill="#e4e4e7" font-weight="500">Total PRs:</text>
    <text x="420" y="192" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#f0f0f0" text-anchor="middle">
      4
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.7s" begin="0.4s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- 统计项 4: Total Issues -->
  <g>
    <circle cx="55" cy="225" r="9" fill="#f87171" opacity="0.15"/>
    <text x="48" y="232" font-size="18">⚠️</text>
    <text x="85" y="232" font-family="'Segoe UI', sans-serif" font-size="17" fill="#e4e4e7" font-weight="500">Total Issues:</text>
    <text x="420" y="232" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#f0f0f0" text-anchor="middle">
      17
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.4s" begin="0.6s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- 统计项 5: Contributed to -->
  <g>
    <circle cx="55" cy="265" r="9" fill="#a78bfa" opacity="0.15"/>
    <text x="48" y="272" font-size="18">💻</text>
    <text x="85" y="272" font-family="'Segoe UI', sans-serif" font-size="17" fill="#e4e4e7" font-weight="500">Contributed to (last year):</text>
    <text x="420" y="272" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="700" fill="#f0f0f0" text-anchor="middle">
      8
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.6s" begin="0.8s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- 右侧环形等级评分 -->
  <g transform="translate(620, 175)">
    <!-- 背景轨道 -->
    <circle cx="0" cy="0" r="64" fill="none" stroke="#3a3c4e" stroke-width="10"/>
    <!-- 进度环 - 动画填充 -->
    <circle cx="0" cy="0" r="64" fill="none" stroke="url(#ringGrad)" stroke-width="10"
      stroke-linecap="round"
      stroke-dasharray="402" stroke-dashoffset="402"
      transform="rotate(-90)">
      <animate attributeName="stroke-dashoffset" values="402;80;80" dur="2s" begin="0.5s" fill="freeze"/>
    </circle>

    <!-- 等级文字 -->
    <text x="0" y="15" font-family="'Segoe UI', sans-serif" font-size="46" font-weight="800" text-anchor="middle" fill="#e94560">
      A-
      <animate attributeName="opacity" values="0;1" dur="0.8s" begin="1.8s" fill="freeze"/>
    </text>
    <text x="0" y="40" font-family="'Segoe UI', sans-serif" font-size="11" text-anchor="middle" fill="#8b8d98" opacity="0">
      GRADE
      <animate attributeName="opacity" values="0;1" dur="0.6s" begin="2.2s" fill="freeze"/>
    </text>
  </g>
</svg>
</div>

<br/>

---

## 🛠 Tech Stack

<!-- 技术栈徽章，纯 SVG 手写，无第三方 -->
<div align="center">
<svg width="780" height="150" viewBox="0 0 780 150">
  <defs>
    <filter id="bShadow" x="-5%" y="-10%" width="110%" height="130%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.15"/>
    </filter>
    <linearGradient id="jsGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f7df1e"/><stop offset="100%" stop-color="#f0b400"/>
    </linearGradient>
    <linearGradient id="tsGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3178c6"/><stop offset="100%" stop-color="#235a97"/>
    </linearGradient>
    <linearGradient id="pyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3776ab"/><stop offset="50%" stop-color="#ffd43b"/><stop offset="100%" stop-color="#306998"/>
    </linearGradient>
    <linearGradient id="goGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00add8"/><stop offset="100%" stop-color="#007d9c"/>
    </linearGradient>
    <linearGradient id="reactGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#61dafb"/><stop offset="100%" stop-color="#20a8ca"/>
    </linearGradient>
    <linearGradient id="vueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#42b883"/><stop offset="100%" stop-color="#35495e"/>
    </linearGradient>
    <linearGradient id="nodeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#339933"/><stop offset="100%" stop-color="#1d5a1d"/>
    </linearGradient>
    <linearGradient id="gitGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f05032"/><stop offset="100%" stop-color="#bc3b1f"/>
    </linearGradient>
    <linearGradient id="dockerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2496ed"/><stop offset="100%" stop-color="#1368a0"/>
    </linearGradient>
    <linearGradient id="sqlGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00758f"/><stop offset="100%" stop-color="#f29111"/>
    </linearGradient>
  </defs>

  <!-- 第一行 -->
  <g font-family="'Segoe UI', sans-serif" font-size="14" font-weight="600" filter="url(#bShadow)">
    <!-- JavaScript -->
    <rect x="10"  y="15" width="130" height="50" rx="12" fill="url(#jsGrad)"/>
    <text x="75"  y="47" fill="#323330" text-anchor="middle">JavaScript</text>

    <!-- TypeScript -->
    <rect x="155" y="15" width="120" height="50" rx="12" fill="url(#tsGrad)"/>
    <text x="215" y="47" fill="#ffffff" text-anchor="middle">TypeScript</text>

    <!-- Python -->
    <rect x="290" y="15" width="110" height="50" rx="12" fill="url(#pyGrad)"/>
    <text x="345" y="47" fill="#ffffff" text-anchor="middle">Python</text>

    <!-- Go -->
    <rect x="415" y="15" width="95"  height="50" rx="12" fill="url(#goGrad)"/>
    <text x="462" y="47" fill="#ffffff" text-anchor="middle">Golang</text>

    <!-- React -->
    <rect x="525" y="15" width="110" height="50" rx="12" fill="url(#reactGrad)"/>
    <text x="580" y="47" fill="#20232a" text-anchor="middle">React</text>

    <!-- Vue -->
    <rect x="650" y="15" width="110" height="50" rx="12" fill="url(#vueGrad)"/>
    <text x="705" y="47" fill="#ffffff" text-anchor="middle">Vue.js</text>
  </g>

  <!-- 第二行 -->
  <g font-family="'Segoe UI', sans-serif" font-size="14" font-weight="600" filter="url(#bShadow)">
    <!-- Node.js -->
    <rect x="10"  y="85" width="110" height="50" rx="12" fill="url(#nodeGrad)"/>
    <text x="65"  y="117" fill="#ffffff" text-anchor="middle">Node.js</text>

    <!-- Git -->
    <rect x="135" y="85" width="85"  height="50" rx="12" fill="url(#gitGrad)"/>
    <text x="177" y="117" fill="#ffffff" text-anchor="middle">Git</text>

    <!-- Docker -->
    <rect x="235" y="85" width="110" height="50" rx="12" fill="url(#dockerGrad)"/>
    <text x="290" y="117" fill="#ffffff" text-anchor="middle">Docker</text>

    <!-- MySQL/SQL -->
    <rect x="360" y="85" width="100" height="50" rx="12" fill="url(#sqlGrad)"/>
    <text x="410" y="117" fill="#ffffff" text-anchor="middle">MySQL</text>

    <!-- HTML5 -->
    <rect x="475" y="85" width="105" height="50" rx="12" fill="#e34f26"/>
    <text x="527" y="117" fill="#ffffff" text-anchor="middle">HTML5</text>

    <!-- CSS3 -->
    <rect x="595" y="85" width="95"  height="50" rx="12" fill="#1572b6"/>
    <text x="642" y="117" fill="#ffffff" text-anchor="middle">CSS3</text>

    <!-- Tailwind -->
    <rect x="705" y="85" width="65"  height="50" rx="12" fill="#06b6d4"/>
    <text x="737" y="117" fill="#0f172a" text-anchor="middle" font-size="12">TW</text>
  </g>
</svg>
</div>

<br/>

---

## 🔗 Connect with me

<div align="center">
  <table>
    <tr>
      <td align="center" width="130">
        <!-- GitHub -->
        <a href="https://github.com/wzxgA" style="text-decoration: none;">
          <svg width="60" height="60" viewBox="0 0 60 60">
            <rect x="5" y="5" width="50" height="50" rx="12" fill="#24292e"/>
            <path d="M30 14 C21.16 14 14 21.16 14 30 c0 7.07 4.58 13.06 10.94 15.18 c0.8 0.15 1.09-0.35 1.09-0.77 c0-0.38-0.02-1.64-0.02-2.98 c-4.45 0.97-5.39-2.14-5.39-2.14 c-0.73-1.85-1.78-2.34-1.78-2.34 c-1.45-0.99 0.11-0.97 0.11-0.97 c1.6 0.12 2.44 1.65 2.44 1.65 c1.43 2.44 3.74 1.73 4.66 1.32 c0.14-1.03 0.55-1.74 1.01-2.14 c-3.55-0.4-7.29-1.78-7.29-7.9 c0-1.75 0.62-3.17 1.64-4.29 c-0.16-0.4-0.71-2.03 0.16-4.23 c0 0 1.34-0.43 4.38 1.63 c1.27-0.35 2.63-0.53 3.98-0.54 c1.35 0.01 2.72 0.19 3.98 0.54 c3.05-2.06 4.38-1.63 4.38-1.63 c0.87 2.2 0.33 3.83 0.16 4.23 c1.02 1.12 1.64 2.54 1.64 4.29 c0 6.13-3.74 7.5-7.3 7.89 c0.57 0.5 1.08 1.47 1.08 2.98 c0 2.15-0.02 3.88-0.02 4.41 c0 0.43 0.29 0.93 1.1 0.77 C41.43 43.05 46 37.07 46 30 C46 21.16 38.84 14 30 14 Z" fill="#fff"/>
          </svg>
          <br/>
          <sub style="color:#6e7681; font-size: 12px;"><b>GitHub</b></sub>
        </a>
      </td>
      <td align="center" width="130">
        <!-- Email -->
        <a href="mailto:wzxgA@example.com" style="text-decoration: none;">
          <svg width="60" height="60" viewBox="0 0 60 60">
            <defs>
              <linearGradient id="emailGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ea4335"/>
                <stop offset="100%" stop-color="#bb001b"/>
              </linearGradient>
            </defs>
            <rect x="5" y="5" width="50" height="50" rx="12" fill="url(#emailGrad)"/>
            <path d="M18 22 L30 32 L42 22 M20 22 L40 22 L40 38 L20 38 Z" fill="none" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/>
          </svg>
          <br/>
          <sub style="color:#6e7681; font-size: 12px;"><b>Email</b></sub>
        </a>
      </td>
      <td align="center" width="130">
        <!-- Blog -->
        <a href="#" style="text-decoration: none;">
          <svg width="60" height="60" viewBox="0 0 60 60">
            <defs>
              <linearGradient id="blogGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#10b981"/>
                <stop offset="100%" stop-color="#047857"/>
              </linearGradient>
            </defs>
            <rect x="5" y="5" width="50" height="50" rx="12" fill="url(#blogGrad)"/>
            <path d="M22 20 L38 20 L38 22 L22 22 Z M22 27 L38 27 L38 29 L22 29 Z M22 34 L32 34 L32 36 L22 36 Z" fill="#fff"/>
            <rect x="17" y="16" width="26" height="28" rx="3" fill="none" stroke="#fff" stroke-width="2"/>
          </svg>
          <br/>
          <sub style="color:#6e7681; font-size: 12px;"><b>Blog</b></sub>
        </a>
      </td>
      <td align="center" width="130">
        <!-- Twitter / X -->
        <a href="#" style="text-decoration: none;">
          <svg width="60" height="60" viewBox="0 0 60 60">
            <rect x="5" y="5" width="50" height="50" rx="12" fill="#000"/>
            <path d="M36 20 L43 20 L28 37 L44 44 L37 44 L23 27 Z M24 24 L30 24 L24 40 L18 40 Z" fill="#fff"/>
          </svg>
          <br/>
          <sub style="color:#6e7681; font-size: 12px;"><b>Twitter</b></sub>
        </a>
      </td>
      <td align="center" width="130">
        <!-- 微信 / WeChat -->
        <svg width="60" height="60" viewBox="0 0 60 60">
          <defs>
            <linearGradient id="wxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#07c160"/>
              <stop offset="100%" stop-color="#05934a"/>
            </linearGradient>
          </defs>
          <rect x="5" y="5" width="50" height="50" rx="12" fill="url(#wxGrad)"/>
          <path d="M22 24 C22 21.24 25.13 19 29 19 C32.5 19 35.4 20.86 36 23.5 C38.6 24.2 40 26.4 40 29 C40 32 37.4 34 34.3 34 L34 34 L33 38 L29 35.8 L29 35 C25.13 35 22 32.76 22 30 C22 29.2 22.17 28.43 22.5 27.7 C22.18 26.5 22 25.28 22 24 Z" fill="none" stroke="#fff" stroke-width="2"/>
          <circle cx="27" cy="26" r="1.5" fill="#fff"/>
          <circle cx="33" cy="26" r="1.5" fill="#fff"/>
        </svg>
        <br/>
        <sub style="color:#6e7681; font-size: 12px;"><b>WeChat</b></sub>
      </td>
    </tr>
  </table>
</div>

<br/>

---

<div align="center">
  <svg width="360" height="60" viewBox="0 0 360 60">
    <text x="180" y="38" font-family="'Segoe UI', 'PingFang SC', sans-serif" font-size="16" text-anchor="middle" fill="#8b8d98">
      Made with
      <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
    </text>
    <text x="220" y="38" font-size="20">
      ❤️
      <animate attributeName="opacity" values="1;0.4;1" dur="1.5s" repeatCount="indefinite"/>
    </text>
    <text x="245" y="38" font-family="'Segoe UI', sans-serif" font-size="16" fill="#8b8d98">by wzxgA</text>
  </svg>
</div>
