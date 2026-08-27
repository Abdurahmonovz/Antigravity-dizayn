import os

styles_data = [
    {
        "name": "MemphisDesign",
        "title": "Memphis Design",
        "desc": "80-yillar uslubi, geometrik shakllar, to'q ranglar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './MemphisDesign.css';

export default function MemphisDesign() {
  return (
    <div className="memphis-page">
      <Navigation title="Memphis Design" description="80-yillar uslubi, geometrik shakllar, to'q ranglar" />
      <main className="memphis-main">
        <div className="memphis-shape shape-1"></div>
        <div className="memphis-shape shape-2"></div>
        <div className="memphis-shape shape-3"></div>
        
        <section className="memphis-hero">
          <h1>MEMPHIS 80s</h1>
          <p>Yorqin, qarama-qarshi ranglar va mavhum geometrik shakllarning erkin uyg'unligi.</p>
        </section>

        <section className="memphis-cards">
          <div className="memphis-card">
            <div className="memphis-icon circle"></div>
            <h2>Geometriya</h2>
            <p>Doiralar, uchburchaklar va zigzag chiziqlar.</p>
          </div>
          <div className="memphis-card">
            <div className="memphis-icon square"></div>
            <h2>Naqshlar</h2>
            <p>Nuqtalar, panjaralar va qora-oq naqshlar asosiysi.</p>
          </div>
          <div className="memphis-card">
            <div className="memphis-icon triangle"></div>
            <h2>Pop Ranglar</h2>
            <p>Neon va qattiq ranglarning kuchli kontrasti.</p>
          </div>
        </section>
      </main>
    </div>
  );
}""",
        "css": """:root { --mem-bg: #ffeb3b; --mem-pink: #ff4081; --mem-cyan: #00e5ff; --mem-purple: #e040fb; }
.memphis-page { min-height: 100vh; padding-top: 100px; background: var(--mem-bg); background-image: radial-gradient(#000 20%, transparent 21%); background-size: 20px 20px; font-family: 'Comic Sans MS', cursive, sans-serif; position: relative; overflow: hidden; }
.memphis-page .style-nav { background: #fff; border-bottom: 4px solid #000; }
.memphis-main { max-width: 1000px; margin: 0 auto; padding: 2rem; position: relative; z-index: 1; }
.memphis-hero { background: var(--mem-pink); border: 5px solid #000; box-shadow: 12px 12px 0 #000; padding: 4rem; text-align: center; color: white; margin-bottom: 4rem; transform: rotate(-2deg); }
.memphis-hero h1 { font-size: 4rem; text-transform: uppercase; text-shadow: 4px 4px 0 var(--mem-cyan); }
.memphis-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 3rem; }
.memphis-card { background: #fff; border: 4px solid #000; box-shadow: 8px 8px 0 #000; padding: 2rem; text-align: center; }
.memphis-card:nth-child(2) { background: var(--mem-cyan); transform: translateY(20px); }
.memphis-card:nth-child(3) { background: var(--mem-purple); color: white; }
.memphis-icon { width: 60px; height: 60px; margin: 0 auto 1rem; border: 4px solid #000; }
.memphis-icon.circle { border-radius: 50%; background: var(--mem-pink); }
.memphis-icon.square { background: var(--mem-bg); }
.memphis-icon.triangle { width: 0; height: 0; border-left: 30px solid transparent; border-right: 30px solid transparent; border-bottom: 50px solid var(--mem-cyan); background: transparent; }
.memphis-shape { position: absolute; border: 4px solid #000; z-index: 0; }
.shape-1 { width: 100px; height: 100px; border-radius: 50%; background: var(--mem-purple); top: 10%; right: 10%; }
.shape-2 { width: 80px; height: 80px; background: var(--mem-cyan); bottom: 20%; left: 5%; transform: rotate(45deg); }
"""
    },
    {
        "name": "VaporwaveY2k",
        "title": "Vaporwave / Y2K",
        "desc": "Neon pushti-binafsha gradientlar, retro-futuristik grafika",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './VaporwaveY2k.css';

export default function VaporwaveY2k() {
  return (
    <div className="vw-page">
      <Navigation title="Vaporwave / Y2K" description="Neon pushti-binafsha gradientlar, retro-futuristik grafika" />
      <div className="vw-sun"></div>
      <div className="vw-grid"></div>
      <main className="vw-main">
        <section className="vw-hero">
          <h1 className="glitch" data-text="A E S T H E T I C">A E S T H E T I C</h1>
          <p>Windows 95, neon quyoshlar va nostalgiya hissiyoti.</p>
        </section>

        <section className="vw-cards">
          <div className="vw-card">
            <h2>Nostalgiya</h2>
            <p>Eski texnologiyalar va 90-yillar romantikasi.</p>
          </div>
          <div className="vw-card">
            <h2>Neon Gradientlar</h2>
            <p>Pushti, binafsha va havorang neon chiziqlar.</p>
          </div>
        </section>
      </main>
    </div>
  );
}""",
        "css": """:root { --vw-pink: #ff71ce; --vw-blue: #01cdfe; --vw-purple: #b967ff; }
.vw-page { min-height: 100vh; padding-top: 100px; background: #000; color: #fff; font-family: 'Courier New', monospace; position: relative; overflow: hidden; }
.vw-page .style-nav { background: rgba(0,0,0,0.8); border-bottom: 2px solid var(--vw-pink); color: var(--vw-blue); text-shadow: 1px 1px var(--vw-pink); }
.vw-grid { position: absolute; bottom: 0; left: -50%; width: 200%; height: 50vh; background-image: linear-gradient(transparent 65%, var(--vw-pink) 66%, var(--vw-pink) 68%, transparent 69%), linear-gradient(90deg, transparent 65%, var(--vw-blue) 66%, var(--vw-blue) 68%, transparent 69%); background-size: 50px 50px; transform: perspective(500px) rotateX(60deg); z-index: 1; }
.vw-sun { position: absolute; bottom: 40vh; left: 50%; transform: translateX(-50%); width: 300px; height: 300px; border-radius: 50%; background: linear-gradient(180deg, #ffeb3b, #ff00ff); box-shadow: 0 0 50px #ff00ff; z-index: 0; }
.vw-main { max-width: 900px; margin: 0 auto; position: relative; z-index: 2; padding: 2rem; text-align: center; }
.vw-hero { margin-top: 5vh; margin-bottom: 10vh; }
.vw-hero h1 { font-size: 5rem; color: #fff; text-shadow: 3px 3px var(--vw-blue), -3px -3px var(--vw-pink); letter-spacing: 5px; margin-bottom: 1rem; }
.vw-cards { display: flex; gap: 2rem; justify-content: center; }
.vw-card { background: rgba(0, 0, 0, 0.7); border: 2px solid var(--vw-blue); box-shadow: inset 0 0 10px var(--vw-pink); padding: 2rem; width: 300px; text-shadow: 1px 1px var(--vw-pink); }
"""
    },
    {
        "name": "CyberpunkSynthwave",
        "title": "Cyberpunk / Synthwave",
        "desc": "Neon nur effektlari, qorong'i fon, elektr ranglar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './CyberpunkSynthwave.css';

export default function CyberpunkSynthwave() {
  return (
    <div className="cp-page">
      <Navigation title="Cyberpunk / Synthwave" description="Neon nur effektlari, qorong'i fon, elektr ranglar" />
      <main className="cp-main">
        <section className="cp-hero">
          <h1 className="cp-glitch">NIGHT CITY</h1>
          <p>High tech, low life. Neon chiroqlar bilan yoritilgan kelajak shahri.</p>
          <button className="cp-btn">SYSTEM_HACK</button>
        </section>

        <section className="cp-cards">
          <div className="cp-card">
            <h2>Neon Nurlar</h2>
            <p>Qorong'i fonda yonib turuvchi sariq, moviy va pushti neon chiziqlar.</p>
          </div>
          <div className="cp-card">
            <h2>Texnologik UI</h2>
            <p>HUD va gologrammalarni eslatuvchi kesilgan burchaklar.</p>
          </div>
        </section>
      </main>
    </div>
  );
}""",
        "css": """:root { --cp-bg: #0d0e15; --cp-yellow: #fcee0a; --cp-cyan: #00f0ff; --cp-pink: #ff003c; }
.cp-page { min-height: 100vh; padding-top: 100px; background: var(--cp-bg); color: var(--cp-yellow); font-family: 'Space Mono', monospace; text-transform: uppercase; }
.cp-page .style-nav { background: #000; border-bottom: 2px solid var(--cp-cyan); color: var(--cp-cyan); }
.cp-main { max-width: 1000px; margin: 0 auto; padding: 2rem; }
.cp-hero { background: rgba(252, 238, 10, 0.1); border: 1px solid var(--cp-yellow); box-shadow: 0 0 15px rgba(252, 238, 10, 0.5); padding: 4rem; text-align: center; margin-bottom: 3rem; clip-path: polygon(0 0, 100% 0, 100% 80%, 95% 100%, 0 100%); }
.cp-hero h1 { font-size: 5rem; text-shadow: 0 0 10px var(--cp-yellow); margin-bottom: 1rem; color: var(--cp-bg); background: var(--cp-yellow); display: inline-block; padding: 0 1rem; }
.cp-btn { background: var(--cp-pink); color: #fff; border: none; padding: 1rem 3rem; font-size: 1.2rem; font-weight: bold; cursor: pointer; clip-path: polygon(10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%, 0 10px); transition: all 0.2s; margin-top: 2rem; }
.cp-btn:hover { background: var(--cp-cyan); color: #000; box-shadow: 0 0 20px var(--cp-cyan); }
.cp-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
.cp-card { border-left: 4px solid var(--cp-cyan); background: rgba(0, 240, 255, 0.05); padding: 2rem; color: var(--cp-cyan); box-shadow: inset 0 0 20px rgba(0, 240, 255, 0.1); }
"""
    },
    {
        "name": "Bauhaus",
        "title": "Bauhaus",
        "desc": "Asosiy geometrik shakllar, asosiy ranglar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './Bauhaus.css';

export default function Bauhaus() {
  return (
    <div className="bauhaus-page">
      <Navigation title="Bauhaus" description="Asosiy geometrik shakllar, asosiy ranglar" />
      <main className="bh-main">
        <section className="bh-hero">
          <div className="bh-shape bh-circle"></div>
          <div className="bh-shape bh-square"></div>
          <div className="bh-shape bh-triangle"></div>
          <div className="bh-hero-content">
            <h1>BAUHAUS</h1>
            <p>Form follows function. Dizayn arxitekturaga aylanadi.</p>
          </div>
        </section>
      </main>
    </div>
  );
}""",
        "css": """:root { --bh-red: #e71d36; --bh-blue: #011627; --bh-yellow: #ff9f1c; --bh-bg: #fdfffc; }
.bauhaus-page { min-height: 100vh; padding-top: 100px; background: var(--bh-bg); font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
.bauhaus-page .style-nav { background: #fff; border-bottom: 5px solid var(--bh-red); }
.bh-main { max-width: 1200px; margin: 0 auto; padding: 2rem; }
.bh-hero { position: relative; height: 70vh; display: flex; align-items: center; justify-content: center; }
.bh-shape { position: absolute; z-index: 1; opacity: 0.9; mix-blend-mode: multiply; }
.bh-circle { width: 400px; height: 400px; background: var(--bh-red); border-radius: 50%; left: 10%; top: 10%; }
.bh-square { width: 350px; height: 350px; background: var(--bh-blue); right: 15%; top: 20%; }
.bh-triangle { width: 0; height: 0; border-left: 200px solid transparent; border-right: 200px solid transparent; border-bottom: 346px solid var(--bh-yellow); left: 35%; bottom: 10%; }
.bh-hero-content { position: relative; z-index: 2; text-align: center; }
.bh-hero-content h1 { font-size: 8rem; font-weight: 800; letter-spacing: -2px; margin: 0; color: #000; mix-blend-mode: overlay; text-shadow: 2px 2px 0 #fff; }
.bh-hero-content p { font-size: 2rem; font-weight: bold; margin-top: 1rem; }
"""
    },
    {
        "name": "ArtDeco",
        "title": "Art Deco",
        "desc": "Nafis, oltin chiziqlar, geometrik naqshlar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './ArtDeco.css';

export default function ArtDeco() {
  return (
    <div className="art-deco-page">
      <Navigation title="Art Deco" description="Nafis, oltin chiziqlar, geometrik naqshlar" />
      <main className="deco-main">
        <div className="deco-border">
          <section className="deco-hero">
            <h1>Gatsby</h1>
            <p>1920-yillarning boyligi va nafosati. Simmetriya va oltin naqshlar.</p>
          </section>
        </div>
      </main>
    </div>
  );
}""",
        "css": """:root { --deco-bg: #0a0a0a; --deco-gold: #c5a059; }
.art-deco-page { min-height: 100vh; padding: 120px 2rem 2rem; background: var(--deco-bg); color: var(--deco-gold); font-family: 'Playfair Display', serif; }
.art-deco-page .style-nav { background: #000; border-bottom: 1px solid var(--deco-gold); color: var(--deco-gold); }
.deco-main { max-width: 800px; margin: 0 auto; height: 70vh; }
.deco-border { border: 2px solid var(--deco-gold); height: 100%; display: flex; align-items: center; justify-content: center; position: relative; padding: 20px; }
.deco-border::before, .deco-border::after { content: ''; position: absolute; width: calc(100% - 20px); height: calc(100% - 20px); border: 1px solid var(--deco-gold); }
.deco-border::before { top: 10px; left: 10px; }
.deco-hero { text-align: center; z-index: 1; }
.deco-hero h1 { font-size: 5rem; font-weight: 400; text-transform: uppercase; letter-spacing: 10px; border-bottom: 2px solid var(--deco-gold); border-top: 2px solid var(--deco-gold); padding: 1rem 0; margin-bottom: 2rem; }
.deco-hero p { font-family: 'Inter', sans-serif; letter-spacing: 2px; text-transform: uppercase; font-size: 0.9rem; }
"""
    },
    {
        "name": "Skeuomorphism",
        "title": "Skeuomorphism",
        "desc": "Real dunyodagi ob'ektlarga o'xshash teksturalar va soyalar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './Skeuomorphism.css';

export default function Skeuomorphism() {
  return (
    <div className="skeuo-page">
      <Navigation title="Skeuomorphism" description="Real dunyodagi ob'ektlarga o'xshash teksturalar" />
      <main className="skeuo-main">
        <div className="skeuo-switch">
          <div className="skeuo-switch-inner">ON</div>
        </div>
        <div className="skeuo-panel">
          <h1>Analog Interfeys</h1>
          <p>Yog'och teksturalar, charm va metall detallar.</p>
          <button className="skeuo-btn">BOSISH</button>
        </div>
      </main>
    </div>
  );
}""",
        "css": """:root { --sk-wood: url('https://www.transparenttextures.com/patterns/wood-pattern.png'); }
.skeuo-page { min-height: 100vh; padding-top: 100px; background-color: #8b5a2b; background-image: var(--sk-wood); color: #222; font-family: 'Georgia', serif; }
.skeuo-page .style-nav { background: linear-gradient(#f9f9f9, #e0e0e0); border-bottom: 2px solid #999; box-shadow: 0 5px 10px rgba(0,0,0,0.5); }
.skeuo-main { max-width: 600px; margin: 2rem auto; }
.skeuo-panel { background: linear-gradient(135deg, #e6e9f0 0%, #eef1f5 100%); padding: 3rem; border-radius: 10px; box-shadow: inset 0 2px 5px rgba(255,255,255,1), 0 10px 20px rgba(0,0,0,0.6); border: 1px solid #999; text-align: center; }
.skeuo-panel h1 { text-shadow: 0 1px 1px #fff; margin-bottom: 1rem; color: #333; }
.skeuo-btn { background: linear-gradient(to bottom, #d4d4d4 0%, #9e9e9e 100%); border: 1px solid #777; border-radius: 5px; padding: 1rem 3rem; font-size: 1.2rem; font-weight: bold; color: #333; text-shadow: 0 1px 1px rgba(255,255,255,0.8); box-shadow: 0 4px 6px rgba(0,0,0,0.5), inset 0 2px 2px rgba(255,255,255,1); transition: all 0.1s; margin-top: 2rem; cursor: pointer; }
.skeuo-btn:active { box-shadow: inset 0 3px 5px rgba(0,0,0,0.6); transform: translateY(2px); background: linear-gradient(to bottom, #9e9e9e 0%, #d4d4d4 100%); }
.skeuo-switch { width: 100px; height: 50px; background: #222; border-radius: 25px; margin: 0 auto 2rem; box-shadow: inset 0 5px 10px rgba(0,0,0,0.8), 0 2px 0 rgba(255,255,255,0.2); position: relative; }
.skeuo-switch-inner { position: absolute; width: 46px; height: 46px; background: linear-gradient(to bottom, #f0f0f0, #ccc); border-radius: 50%; right: 2px; top: 2px; box-shadow: -2px 0 5px rgba(0,0,0,0.3), inset 0 2px 2px rgba(255,255,255,1); display: flex; align-items: center; justify-content: center; font-size: 0.6rem; color: #4caf50; font-weight: bold; }
"""
    },
    {
        "name": "BentoGrid",
        "title": "Bento Grid",
        "desc": "Turli o'lchamdagi to'rtburchak bloklar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './BentoGrid.css';

export default function BentoGrid() {
  return (
    <div className="bento-page">
      <Navigation title="Bento Grid" description="Bento qutisi kabi tartibli bloklar" />
      <main className="bento-main">
        <div className="bento-grid-container">
          <div className="bento-item hero-item">
            <h1>Bento UI</h1>
            <p>Ma'lumotlarni ixcham va vizual tartibda yetkazish usuli.</p>
          </div>
          <div className="bento-item image-item">Surat</div>
          <div className="bento-item stat-item">
            <h2>99%</h2>
            <p>Samaradorlik</p>
          </div>
          <div className="bento-item wide-item">Yana bir muhim xabar</div>
          <div className="bento-item square-item">A</div>
          <div className="bento-item square-item">B</div>
        </div>
      </main>
    </div>
  );
}""",
        "css": """:root { --bg-bg: #f3f4f6; }
.bento-page { min-height: 100vh; padding-top: 100px; background: var(--bg-bg); font-family: 'Inter', sans-serif; }
.bento-page .style-nav { background: #fff; border-bottom: 1px solid #e5e7eb; }
.bento-main { max-width: 900px; margin: 0 auto; padding: 2rem; }
.bento-grid-container { display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 200px; gap: 1.5rem; }
.bento-item { background: #fff; border-radius: 24px; padding: 2rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: center; }
.hero-item { grid-column: span 2; grid-row: span 2; background: #3b82f6; color: white; }
.hero-item h1 { font-size: 3rem; margin-bottom: 1rem; }
.image-item { grid-column: span 2; background: #fca5a5; }
.stat-item { background: #34d399; color: white; align-items: center; }
.stat-item h2 { font-size: 3rem; }
.wide-item { grid-column: span 2; background: #a78bfa; color: white; }
.square-item { align-items: center; font-size: 2rem; font-weight: bold; background: #fbcfe8; }
@media (max-width: 768px) { .bento-grid-container { grid-template-columns: 1fr; } .hero-item, .image-item, .wide-item { grid-column: span 1; } }
"""
    },
    {
        "name": "AuroraGradientMesh",
        "title": "Aurora / Gradient Mesh",
        "desc": "Yumshoq, ko'p rangli gradient fonlar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './AuroraGradientMesh.css';

export default function AuroraGradientMesh() {
  return (
    <div className="aurora-page">
      <div className="aurora-bg"></div>
      <Navigation title="Aurora" description="Yumshoq gradientlar va organik shakllar" />
      <main className="aurora-main">
        <section className="aurora-glass">
          <h1>Gradient Mesh</h1>
          <p>Yorug'lik nurlari kabi o'zgaruvchi va oqib o'tuvchi yumshoq ranglar.</p>
        </section>
      </main>
    </div>
  );
}""",
        "css": """:root { --aurora-1: #ffb7b2; --aurora-2: #e2f0cb; --aurora-3: #b5ead7; --aurora-4: #c7ceea; }
.aurora-page { min-height: 100vh; padding-top: 100px; position: relative; overflow: hidden; font-family: 'Outfit', sans-serif; }
.aurora-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; background: linear-gradient(125deg, var(--aurora-1), var(--aurora-2), var(--aurora-3), var(--aurora-4)); background-size: 400% 400%; animation: gradientMesh 15s ease infinite; }
@keyframes gradientMesh { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
.aurora-page .style-nav { background: rgba(255,255,255,0.2); backdrop-filter: blur(10px); border: none; }
.aurora-main { position: relative; z-index: 1; max-width: 800px; margin: 10vh auto; padding: 2rem; text-align: center; }
.aurora-glass { background: rgba(255, 255, 255, 0.4); backdrop-filter: blur(20px); border: 1px solid rgba(255, 255, 255, 0.5); padding: 5rem 3rem; border-radius: 30px; color: #333; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.aurora-glass h1 { font-size: 4rem; margin-bottom: 1rem; color: #fff; text-shadow: 0 2px 10px rgba(0,0,0,0.1); }
.aurora-glass p { font-size: 1.25rem; font-weight: 500; }
"""
    },
    {
        "name": "RetroFuturism",
        "title": "Retro-Futurism",
        "desc": "60-70-yillar kelajak tasavvuri, pastel ranglar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './RetroFuturism.css';

export default function RetroFuturism() {
  return (
    <div className="retro-page">
      <Navigation title="Retro-Futurism" description="60-70-yillar kelajak tasavvuri" />
      <main className="retro-main">
        <section className="retro-hero">
          <h1>SPACE AGE</h1>
          <p>Yumshoq pastel ranglar va qalin yumaloq shriftlar.</p>
          <div className="retro-circles">
            <div className="circle c1"></div>
            <div className="circle c2"></div>
            <div className="circle c3"></div>
          </div>
        </section>
      </main>
    </div>
  );
}""",
        "css": """:root { --rf-bg: #ffecd2; --rf-orange: #fcb69f; --rf-text: #4a4a4a; }
.retro-page { min-height: 100vh; padding-top: 100px; background: var(--rf-bg); color: var(--rf-text); font-family: 'Outfit', sans-serif; }
.retro-page .style-nav { background: var(--rf-orange); border-bottom: 3px solid #fff; }
.retro-main { max-width: 800px; margin: 2rem auto; text-align: center; }
.retro-hero { background: #fff; padding: 4rem; border-radius: 50px; border: 5px solid var(--rf-orange); box-shadow: 10px 10px 0 var(--rf-orange); }
.retro-hero h1 { font-size: 4rem; color: var(--rf-orange); letter-spacing: 5px; margin-bottom: 1rem; }
.retro-circles { display: flex; justify-content: center; gap: 1rem; margin-top: 3rem; }
.retro-circles .circle { width: 50px; height: 50px; border-radius: 50%; background: var(--rf-orange); }
.c1 { opacity: 0.5; } .c2 { opacity: 0.7; } .c3 { opacity: 1; }
"""
    },
    {
        "name": "EditorialMagazineStyle",
        "title": "Editorial / Magazine",
        "desc": "Jurnal maketiga o'xshash, katta tipografika",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './EditorialMagazineStyle.css';

export default function EditorialMagazineStyle() {
  return (
    <div className="editorial-page">
      <Navigation title="Editorial Style" description="Jurnal maketiga o'xshash, katta tipografika" />
      <main className="ed-main">
        <header className="ed-header">
          <h1>THE VOGUE</h1>
          <div className="ed-meta">№ 01 — 2026 ISSUE</div>
        </header>
        <article className="ed-content">
          <div className="ed-col main-col">
            <h2>Elegance is an Attitude.</h2>
            <p className="ed-dropcap">Dizayndagi har bir chiziq va shrift tanlovi o'zining noyob xarakterini ko'rsatadi. Jurnal maketlarida asosan ustunli tizim, katta sarlavhalar va serif shriftlar ustunlik qiladi. Bularning barchasi foydalanuvchiga xuddi kitob yoki sifatli nashrni o'qiyotgandek hissini beradi.</p>
          </div>
          <div className="ed-col side-col">
            <h3>Fashion & Web</h3>
            <p>Veb dizayn va bosma nashrlar qoidalari tobora birlashib bormoqda.</p>
          </div>
        </article>
      </main>
    </div>
  );
}""",
        "css": """:root { --ed-bg: #f8f8f8; --ed-text: #1a1a1a; }
.editorial-page { min-height: 100vh; padding-top: 100px; background: var(--ed-bg); color: var(--ed-text); font-family: 'Playfair Display', serif; }
.editorial-page .style-nav { background: #fff; border-bottom: 1px solid #ddd; }
.ed-main { max-width: 1000px; margin: 0 auto; padding: 2rem; }
.ed-header { text-align: center; border-bottom: 4px solid #000; border-top: 1px solid #000; padding: 3rem 0 1rem; margin-bottom: 3rem; }
.ed-header h1 { font-size: 6rem; font-weight: 700; letter-spacing: -2px; margin: 0; line-height: 1; }
.ed-meta { font-family: 'Inter', sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 1rem; color: #666; }
.ed-content { display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; }
.ed-col h2 { font-size: 3rem; font-weight: 400; line-height: 1.1; margin-bottom: 1.5rem; }
.ed-col h3 { font-size: 1.5rem; border-top: 2px solid #000; padding-top: 1rem; margin-bottom: 1rem; }
.ed-col p { font-family: 'Inter', sans-serif; line-height: 1.6; color: #444; }
.ed-dropcap::first-letter { float: left; font-size: 4rem; font-family: 'Playfair Display', serif; line-height: 0.8; padding-right: 0.5rem; font-weight: bold; }
"""
    },
    {
        "name": "CorporateMemphis",
        "title": "Corporate Memphis",
        "desc": "Soddalashtirilgan inson figuralari, tekis ranglar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './CorporateMemphis.css';

export default function CorporateMemphis() {
  return (
    <div className="cm-page">
      <Navigation title="Corporate Memphis" description="Soddalashtirilgan inson figuralari, tekis ranglar" />
      <main className="cm-main">
        <div className="cm-illustration">
          <div className="cm-person"></div>
          <div className="cm-plant"></div>
        </div>
        <section className="cm-content">
          <h1>Biznesingizni o'stiring</h1>
          <p>Do'stona, optimistik va texnologik kompaniyalar uchun eng mos vizual uslub (Alegria).</p>
          <button className="cm-btn">Boshlash</button>
        </section>
      </main>
    </div>
  );
}""",
        "css": """:root { --cm-bg: #f3f0ff; --cm-purple: #6c5ce7; --cm-yellow: #fdcb6e; --cm-blue: #0984e3; --cm-green: #00b894; }
.cm-page { min-height: 100vh; padding-top: 100px; background: var(--cm-bg); font-family: 'Inter', sans-serif; }
.cm-page .style-nav { background: #fff; border-bottom: 1px solid #ddd; }
.cm-main { max-width: 1000px; margin: 2rem auto; display: flex; align-items: center; justify-content: space-between; padding: 2rem; gap: 4rem; }
.cm-content { flex: 1; }
.cm-content h1 { font-size: 3.5rem; color: #2d3436; margin-bottom: 1rem; line-height: 1.2; }
.cm-content p { font-size: 1.25rem; color: #636e72; margin-bottom: 2rem; }
.cm-btn { background: var(--cm-purple); color: #fff; padding: 1rem 2.5rem; font-size: 1.1rem; border-radius: 8px; border: none; font-weight: 600; cursor: pointer; transition: transform 0.2s; }
.cm-btn:hover { transform: translateY(-2px); }
.cm-illustration { flex: 1; height: 400px; position: relative; background: #fff; border-radius: 20px; box-shadow: 0 20px 40px rgba(108, 92, 231, 0.1); }
.cm-person { position: absolute; width: 60px; height: 180px; background: var(--cm-blue); border-radius: 30px; bottom: 20px; left: 100px; }
.cm-person::before { content: ''; position: absolute; width: 50px; height: 50px; background: var(--cm-yellow); border-radius: 50%; top: -60px; left: 5px; }
.cm-plant { position: absolute; width: 40px; height: 100px; background: var(--cm-green); border-radius: 40px 0 40px 0; bottom: 20px; right: 80px; }
"""
    },
    {
        "name": "KineticTypography",
        "title": "Kinetic Typography",
        "desc": "Harakatlanuvchi matn va animatsiyalar",
        "jsx": """import React from 'react';
import Navigation from '../../components/Navigation';
import './KineticTypography.css';

export default function KineticTypography() {
  return (
    <div className="kt-page">
      <Navigation title="Kinetic Typography" description="Harakatlanuvchi matn" />
      <main className="kt-main">
        <div className="marquee">
          <div className="marquee-inner">
            <span>MOTION IS EMOTION • TYPOGRAPHY • </span>
            <span>MOTION IS EMOTION • TYPOGRAPHY • </span>
          </div>
        </div>
        <div className="marquee reverse">
          <div className="marquee-inner">
            <span>DESIGN THAT MOVES • ANIMATION • </span>
            <span>DESIGN THAT MOVES • ANIMATION • </span>
          </div>
        </div>
      </main>
    </div>
  );
}""",
        "css": """:root { --kt-bg: #000; --kt-text: #fff; }
.kt-page { min-height: 100vh; padding-top: 100px; background: var(--kt-bg); font-family: 'Inter', sans-serif; overflow: hidden; }
.kt-page .style-nav { background: #111; border-bottom: 1px solid #333; color: #fff; }
.kt-page .style-nav .nav-back, .kt-page .style-nav .badge-desc { color: #888; }
.kt-main { margin-top: 10vh; }
.marquee { width: 100vw; overflow: hidden; border-top: 1px solid #333; border-bottom: 1px solid #333; padding: 1rem 0; margin-bottom: 2rem; background: #0a0a0a; }
.marquee-inner { display: flex; width: max-content; animation: marquee 10s linear infinite; }
.marquee.reverse .marquee-inner { animation-direction: reverse; background: #fff; color: #000; }
.marquee span { font-size: 5rem; font-weight: 900; white-space: nowrap; padding-right: 2rem; letter-spacing: -2px; }
@keyframes marquee { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-50%, 0, 0); } }
"""
    }
]

for style in styles_data:
    name = style["name"]
    jsx_content = style["jsx"]
    css_content = style["css"]
    
    with open(f"src/pages/styles/{name}.jsx", "w") as f:
        f.write(jsx_content)
        
    with open(f"src/pages/styles/{name}.css", "w") as f:
        f.write(css_content)

print(f"Generated {len(styles_data)} styles fully.")
