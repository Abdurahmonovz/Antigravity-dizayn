import React from 'react';
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
}