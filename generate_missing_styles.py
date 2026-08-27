import json

# Generate specific CSS contents for the remaining 14 styles
css_templates = {
    "MaterialDesign": """:root { --md-primary: #6200ea; --md-bg: #f5f5f5; }
.materialdesign-page { min-height: 100vh; padding-top: 80px; background: var(--md-bg); font-family: Roboto, sans-serif; }
.demo-hero { background: var(--md-primary); color: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); padding: 4rem; text-align: center; margin-bottom: 2rem; margin-top: 2rem; }
.demo-cards { display: grid; gap: 2rem; grid-template-columns: 1fr 1fr 1fr; }
.demo-card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: box-shadow 0.3s; }
.demo-card:hover { box-shadow: 0 8px 16px rgba(0,0,0,0.2); }
""",
    "FlatDesign2": """:root { --fd-primary: #2ecc71; --fd-bg: #ecf0f1; --fd-text: #2c3e50; }
.flatdesign2-page { min-height: 100vh; padding-top: 80px; background: var(--fd-bg); color: var(--fd-text); }
.demo-hero { background: var(--fd-primary); color: white; padding: 4rem; text-align: center; margin-top: 2rem; }
.demo-card { background: white; padding: 2rem; border: none; box-shadow: none; }
""",
    "MemphisDesign": """:root { --mem-bg: #ffeb3b; --mem-pink: #ff4081; --mem-cyan: #00e5ff; }
.memphisdesign-page { min-height: 100vh; padding-top: 80px; background: var(--mem-bg); background-image: radial-gradient(#000 10%, transparent 11%); background-size: 20px 20px; font-family: 'Comic Sans MS', sans-serif; }
.demo-hero { background: var(--mem-pink); color: white; border: 4px solid black; box-shadow: 10px 10px 0 black; margin-top: 2rem; padding: 4rem; }
.demo-card { background: var(--mem-cyan); border: 4px solid black; padding: 2rem; border-radius: 50%; text-align: center; }
""",
    "VaporwaveY2k": """:root { --vw-bg: linear-gradient(180deg, #ff71ce, #01cdfe); }
.vaporwavey2k-page { min-height: 100vh; padding-top: 80px; background: var(--vw-bg); color: white; font-family: 'Courier New', monospace; text-shadow: 2px 2px #ff00ff; }
.demo-hero { background: rgba(0,0,0,0.5); padding: 4rem; margin-top: 2rem; border: 2px solid cyan; }
.demo-card { background: rgba(255,255,255,0.2); backdrop-filter: blur(5px); border: 1px solid pink; padding: 2rem; }
""",
    "CyberpunkSynthwave": """:root { --cp-bg: #000000; --cp-neon-yellow: #fcee0a; --cp-neon-blue: #01cdfe; }
.cyberpunksynthwave-page { min-height: 100vh; padding-top: 80px; background: var(--cp-bg); color: var(--cp-neon-yellow); font-family: monospace; text-transform: uppercase; }
.demo-hero { border: 2px solid var(--cp-neon-yellow); box-shadow: 0 0 10px var(--cp-neon-yellow); margin-top: 2rem; padding: 4rem; background: #111; clip-path: polygon(0 0, 100% 0, 100% 80%, 90% 100%, 0 100%); }
.demo-card { border: 1px solid var(--cp-neon-blue); color: var(--cp-neon-blue); box-shadow: 0 0 5px var(--cp-neon-blue); padding: 2rem; background: #050505; }
""",
    "Bauhaus": """:root { --bh-bg: #ffffff; --bh-red: #ff0000; --bh-blue: #0000ff; --bh-yellow: #ffff00; }
.bauhaus-page { min-height: 100vh; padding-top: 80px; background: var(--bh-bg); font-family: 'Arial', sans-serif; }
.demo-hero { background: var(--bh-red); color: white; padding: 4rem; border-radius: 0; margin-top: 2rem; }
.demo-card:nth-child(1) { background: var(--bh-blue); color: white; border-radius: 50%; }
.demo-card:nth-child(2) { background: var(--bh-yellow); color: black; border-radius: 0; }
.demo-card:nth-child(3) { background: var(--bh-red); color: white; border-radius: 0; clip-path: polygon(50% 0%, 0% 100%, 100% 100%); }
.demo-card { padding: 3rem; text-align: center; margin: 1rem; }
""",
    "ArtDeco": """:root { --ad-bg: #000000; --ad-gold: #d4af37; }
.artdeco-page { min-height: 100vh; padding-top: 80px; background: var(--ad-bg); color: var(--ad-gold); font-family: 'Playfair Display', serif; }
.demo-hero { border: 4px double var(--ad-gold); padding: 4rem; margin-top: 2rem; background: #111; text-align: center; }
.demo-card { border: 2px solid var(--ad-gold); padding: 2rem; background: #050505; }
""",
    "Skeuomorphism": """:root { --sk-bg: #d2b48c; }
.skeuomorphism-page { min-height: 100vh; padding-top: 80px; background: var(--sk-bg); background-image: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(0,0,0,0.05) 10px, rgba(0,0,0,0.05) 20px); font-family: 'Georgia', serif; }
.demo-hero { background: linear-gradient(to bottom, #f5f5dc, #d2b48c); border: 2px solid #8b4513; border-radius: 15px; box-shadow: inset 0 2px 5px rgba(255,255,255,0.7), 0 5px 15px rgba(0,0,0,0.5); padding: 4rem; margin-top: 2rem; }
.demo-card { background: linear-gradient(to bottom, #ffffff, #e0e0e0); border: 1px solid #999; border-radius: 10px; box-shadow: inset 0 1px 0 white, 0 4px 6px rgba(0,0,0,0.3); padding: 2rem; text-align: center; }
""",
    "BentoGrid": """:root { --bento-bg: #f3f4f6; }
.bentogrid-page { min-height: 100vh; padding-top: 80px; background: var(--bento-bg); font-family: 'Inter', sans-serif; }
.demo-hero { grid-column: span 3; background: white; padding: 4rem; border-radius: 20px; margin-top: 2rem; margin-bottom: 2rem; }
.demo-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.demo-card { background: white; border-radius: 20px; padding: 2rem; }
.demo-card:nth-child(1) { grid-column: span 2; }
""",
    "AuroraGradientMesh": """:root { --aur-bg: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%); }
.auroragradientmesh-page { min-height: 100vh; padding-top: 80px; background: var(--aur-bg); font-family: 'Outfit', sans-serif; }
.demo-hero { background: rgba(255,255,255,0.2); backdrop-filter: blur(10px); padding: 4rem; border-radius: 30px; margin-top: 2rem; color: #fff; }
.demo-card { background: rgba(255,255,255,0.3); backdrop-filter: blur(5px); border-radius: 20px; padding: 2rem; color: #fff; }
""",
    "RetroFuturism": """:root { --rf-bg: #ff9a9e; }
.retrofuturism-page { min-height: 100vh; padding-top: 80px; background: var(--rf-bg); font-family: 'Space Mono', monospace; }
.demo-hero { background: #fecfef; border-radius: 50px; padding: 4rem; margin-top: 2rem; border: 5px solid white; color: #333; }
.demo-card { background: white; border-radius: 30px; padding: 2rem; color: #ff9a9e; }
""",
    "EditorialMagazineStyle": """:root { --ed-bg: #ffffff; --ed-text: #000000; }
.editorialmagazinestyle-page { min-height: 100vh; padding-top: 80px; background: var(--ed-bg); color: var(--ed-text); font-family: 'Playfair Display', serif; }
.demo-hero { padding: 4rem 0; margin-top: 2rem; border-bottom: 2px solid black; border-top: 8px solid black; }
.demo-hero h1 { font-size: 5rem; text-transform: uppercase; letter-spacing: -2px; }
.demo-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; margin-top: 2rem; }
.demo-card { padding: 0; background: transparent; }
.demo-card h2 { font-size: 2rem; margin-bottom: 1rem; }
""",
    "CorporateMemphis": """:root { --cm-bg: #f9f9f9; --cm-purple: #6c5ce7; }
.corporatememphis-page { min-height: 100vh; padding-top: 80px; background: var(--cm-bg); font-family: 'Inter', sans-serif; }
.demo-hero { background: var(--cm-purple); color: white; border-radius: 24px; padding: 4rem; margin-top: 2rem; }
.demo-card { background: white; border-radius: 16px; padding: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
""",
    "KineticTypography": """:root { --kt-bg: #111111; --kt-text: #ffffff; }
.kinetictypography-page { min-height: 100vh; padding-top: 80px; background: var(--kt-bg); color: var(--kt-text); font-family: 'Outfit', sans-serif; overflow: hidden; }
.demo-hero { padding: 4rem; margin-top: 2rem; background: transparent; }
.demo-hero h1 { font-size: 6rem; white-space: nowrap; animation: slide 10s linear infinite; }
@keyframes slide { from { transform: translateX(100%); } to { transform: translateX(-100%); } }
.demo-card { background: #222; padding: 2rem; border-radius: 0; }
"""
}

import os
for name, content in css_templates.items():
    file_path = f"src/pages/styles/{name}.css"
    if os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(content)

print("Updated 14 CSS styles")
