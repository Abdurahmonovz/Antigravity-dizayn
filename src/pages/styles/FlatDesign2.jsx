import React from 'react';
import Navigation from '../../components/Navigation';
import './FlatDesign2.css';

export default function FlatDesign2() {
  return (
    <div className="flat-page">
      <Navigation 
        title="Flat Design 2.0" 
        description="Soyasiz, tekis ranglar, biroz chuqurlik, sodda ikonkalar"
      />
      
      <main className="flat-main">
        <section className="flat-hero">
          <div className="flat-illustration">
            <div className="flat-circle"></div>
            <div className="flat-square"></div>
            <div className="flat-triangle"></div>
          </div>
          <h1>Flat Design 2.0 (Semi-Flat)</h1>
          <p>Asl Flat Design qoidalarini saqlagan holda yengil soyalar va nozik gradientlar yordamida yorqin, ishonchli va tezkor interfeys.</p>
          <button className="flat-btn">Hoziroq Bosish</button>
        </section>

        <section className="flat-cards">
          <div className="flat-card flat-card-green">
            <h2>Qattiq va Yorqin Ranglar</h2>
            <p>Elementlarni ajratish uchun sof, quyuq rang palitrasi.</p>
          </div>
          <div className="flat-card flat-card-blue">
            <h2>Minimal Soya</h2>
            <p>1.0 dan farqli ravishda tugmalar orqasida yengil va yumshoq soya.</p>
          </div>
          <div className="flat-card flat-card-red">
            <h2>Oddiy Shriftlar</h2>
            <p>Katta o'lchamli sans-serif shriftlar orqali oson o'qiluvchi kontent.</p>
          </div>
        </section>
      </main>
    </div>
  );
}
