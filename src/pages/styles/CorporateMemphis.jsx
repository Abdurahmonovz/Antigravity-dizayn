import React from 'react';
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
}