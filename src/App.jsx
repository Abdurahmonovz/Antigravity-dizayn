import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import NeoBrutalism from './pages/styles/NeoBrutalism';
import Glassmorphism from './pages/styles/Glassmorphism';
import Neumorphism from './pages/styles/Neumorphism';
import Claymorphism from './pages/styles/Claymorphism';
import Minimalism from './pages/styles/Minimalism';
import MaterialDesign from './pages/styles/MaterialDesign';
import FlatDesign2 from './pages/styles/FlatDesign2';
import DarkModeLuxury from './pages/styles/DarkModeLuxury';
import MemphisDesign from './pages/styles/MemphisDesign';
import VaporwaveY2k from './pages/styles/VaporwaveY2k';
import CyberpunkSynthwave from './pages/styles/CyberpunkSynthwave';
import Bauhaus from './pages/styles/Bauhaus';
import ArtDeco from './pages/styles/ArtDeco';
import Skeuomorphism from './pages/styles/Skeuomorphism';
import BentoGrid from './pages/styles/BentoGrid';
import AuroraGradientMesh from './pages/styles/AuroraGradientMesh';
import RetroFuturism from './pages/styles/RetroFuturism';
import EditorialMagazineStyle from './pages/styles/EditorialMagazineStyle';
import CorporateMemphis from './pages/styles/CorporateMemphis';
import KineticTypography from './pages/styles/KineticTypography';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/styles/neo-brutalism" element={<NeoBrutalism />} />
      <Route path="/styles/glassmorphism" element={<Glassmorphism />} />
      <Route path="/styles/neumorphism" element={<Neumorphism />} />
      <Route path="/styles/claymorphism" element={<Claymorphism />} />
      <Route path="/styles/minimalism" element={<Minimalism />} />
      <Route path="/styles/material-design" element={<MaterialDesign />} />
      <Route path="/styles/flat-design" element={<FlatDesign2 />} />
      <Route path="/styles/dark-mode-luxury" element={<DarkModeLuxury />} />
      <Route path="/styles/memphis" element={<MemphisDesign />} />
      <Route path="/styles/vaporwave" element={<VaporwaveY2k />} />
      <Route path="/styles/cyberpunk" element={<CyberpunkSynthwave />} />
      <Route path="/styles/bauhaus" element={<Bauhaus />} />
      <Route path="/styles/art-deco" element={<ArtDeco />} />
      <Route path="/styles/skeuomorphism" element={<Skeuomorphism />} />
      <Route path="/styles/bento-grid" element={<BentoGrid />} />
      <Route path="/styles/aurora" element={<AuroraGradientMesh />} />
      <Route path="/styles/retro-futurism" element={<RetroFuturism />} />
      <Route path="/styles/editorial" element={<EditorialMagazineStyle />} />
      <Route path="/styles/corporate-memphis" element={<CorporateMemphis />} />
      <Route path="/styles/kinetic" element={<KineticTypography />} />
    </Routes>
  );
}

export default App;
