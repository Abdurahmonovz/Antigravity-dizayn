import React from 'react';
import { designStyles } from '../data/styles';
import StyleCard from '../components/StyleCard';

export default function Home() {
  return (
    <div className="home-page">
      <header className="gallery-header">
        <h1>Dizayn Uslublari Galereyasi</h1>
        <p>Antigravityda o'z saytingizni dizaynini mana shu bo'limlardagi nomlar orqali o'z saytingizni jonlantiring!</p>
        <a href="https://t.me/Antigravity_tekshir_bot?start=1" target="_blank" rel="noopener noreferrer" className="telegram-btn">
          Bundanda qiziq ma'lumotlarni olish uchun tugmani bosing
        </a>
      </header>
      
      <main className="gallery-grid">
        {designStyles.map(style => (
          <StyleCard key={style.id} style={style} />
        ))}
      </main>
    </div>
  );
}
