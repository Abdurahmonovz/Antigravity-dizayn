import json

styles = [
  {"id": "neumorphism", "name": "Neumorphism", "description": "Bir xil fon rangida bo'rtma va botiq soyalar"},
  {"id": "claymorphism", "name": "Claymorphism", "description": "3D, 'loydan yasalgan' kabi yumshoq va bo'rtib turgan elementlar"},
  {"id": "minimalism", "name": "Minimalism", "description": "Ko'p bo'sh joy, oq fon, aniq tipografika, minimal ranglar"},
  {"id": "material-design", "name": "Material Design", "description": "Google uslubi: soyalar, elevatsiya, dumaloq burchaklar"},
  {"id": "flat-design", "name": "Flat Design 2.0", "description": "Soyasiz, tekis ranglar, sodda ikonkalar"},
  {"id": "dark-mode-luxury", "name": "Dark Mode Luxury", "description": "Qora fon, oltin/kumush aksent ranglar, nafis tipografika"},
  {"id": "memphis", "name": "Memphis Design", "description": "80-yillar uslubi, geometrik shakllar, to'q ranglar"},
  {"id": "vaporwave", "name": "Vaporwave / Y2K", "description": "Neon pushti-binafsha gradientlar, retro-futuristik grafika"},
  {"id": "cyberpunk", "name": "Cyberpunk / Synthwave", "description": "Neon nur effektlari, qorong'i fon, elektr ranglar"},
  {"id": "bauhaus", "name": "Bauhaus", "description": "Asosiy geometrik shakllar (doira, kvadrat, uchburchak)"},
  {"id": "art-deco", "name": "Art Deco", "description": "Nafis, oltin chiziqlar, geometrik naqshlar, lyuks tuyg'usi"},
  {"id": "skeuomorphism", "name": "Skeuomorphism", "description": "Real dunyodagi ob'ektlarga o'xshash teksturalar va soyalar"},
  {"id": "bento-grid", "name": "Bento Grid", "description": "Turli o'lchamdagi to'rtburchak bloklardan tashkil topgan grid"},
  {"id": "aurora", "name": "Aurora / Gradient Mesh", "description": "Yumshoq, ko'p rangli gradient fonlar, organik shakllar"},
  {"id": "retro-futurism", "name": "Retro-Futurism", "description": "60-70-yillar kelajak tasavvuri, pastel ranglar"},
  {"id": "editorial", "name": "Editorial / Magazine Style", "description": "Jurnal maketiga o'xshash, katta tipografika, ustunli joylashuv"},
  {"id": "corporate-memphis", "name": "Corporate Memphis", "description": "Soddalashtirilgan inson figuralari, tekis ranglar"},
  {"id": "kinetic", "name": "Kinetic Typography", "description": "Harakatlanuvchi matn va animatsiyalar asosidagi dizayn"}
]

app_routes = []
app_imports = [
    "import React from 'react';",
    "import { Routes, Route } from 'react-router-dom';",
    "import Home from './pages/Home';",
    "import NeoBrutalism from './pages/styles/NeoBrutalism';",
    "import Glassmorphism from './pages/styles/Glassmorphism';"
]

app_routes.append('<Route path="/" element={<Home />} />')
app_routes.append('<Route path="/styles/neo-brutalism" element={<NeoBrutalism />} />')
app_routes.append('<Route path="/styles/glassmorphism" element={<Glassmorphism />} />')

for style in styles:
    component_name = "".join([word.capitalize() for word in style["name"].replace("/", " ").replace("-", " ").split()])
    
    # JSX
    jsx_content = f"""import React from 'react';
import Navigation from '../../components/Navigation';
import './{component_name}.css';

export default function {component_name}() {{
  return (
    <div className="{{'{component_name.lower()}-page'}}">
      <Navigation 
        title="{style['name']}" 
        description="{style['description']}"
      />
      
      <main className="demo-main">
        <section className="demo-hero">
          <h1>{style['name']}</h1>
          <p>{style['description']}</p>
          <button>Boshlash</button>
        </section>

        <section className="demo-cards">
          <div className="demo-card">
            <h2>Xususiyat 1</h2>
            <p>Tavsif bu yerda bo'ladi.</p>
          </div>
          <div className="demo-card">
            <h2>Xususiyat 2</h2>
            <p>Tavsif bu yerda bo'ladi.</p>
          </div>
          <div className="demo-card">
            <h2>Xususiyat 3</h2>
            <p>Tavsif bu yerda bo'ladi.</p>
          </div>
        </section>
      </main>
    </div>
  );
}}
"""
    with open(f"src/pages/styles/{component_name}.jsx", "w") as f:
        f.write(jsx_content)

    # CSS
    css_content = f""".{component_name.lower()}-page {{
  min-height: 100vh;
  padding-top: 80px;
}}
.demo-main {{
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
}}
.demo-hero {{
  text-align: center;
  margin-bottom: 3rem;
  padding: 4rem;
  background: #f1f5f9;
  border-radius: 12px;
}}
.demo-cards {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}}
.demo-card {{
  padding: 2rem;
  background: #f1f5f9;
  border-radius: 12px;
}}
"""
    with open(f"src/pages/styles/{component_name}.css", "w") as f:
        f.write(css_content)

    # App imports and routes
    app_imports.append(f"import {component_name} from './pages/styles/{component_name}';")
    app_routes.append(f'<Route path="/styles/{style["id"]}" element={{<{component_name} />}} />')

# Write App.jsx
app_jsx_content = "\n".join(app_imports) + "\n\n" + "function App() {\n  return (\n    <Routes>\n      " + "\n      ".join(app_routes) + "\n    </Routes>\n  );\n}\n\nexport default App;\n"

with open("src/App.jsx", "w") as f:
    f.write(app_jsx_content)

print("Generated all styles!")
