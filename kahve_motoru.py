#!/usr/bin/env python3
# Abartılı Kahve Felsefe Motoru
# Bu kod gerçekten çalışır, ama çok yavaş. Kahve gibi.

import time
import random
import sys

def yudum_al():
    print("\n☕ Kahve yudumlanıyor... (bu 3 saniye sürer, gerçek hayatta daha uzun)")
    time.sleep(3)
    print("*yudum* Felsefe aktive oluyor...")

def felsefe_uret(soru):
    yudum_al()
    felsefeler = [
        f"'{soru}' sorusu, aslında evrenin en büyük sırrıdır. Kahvenin köpüğünde gizli.",
        f"Bu soruyu düşünürken kahvem soğudu. Hayat da böyle soğur.",
        f"Cevap: {random.choice(['Belki', 'Hayır', 'Evet ama yavaşça', 'Kahve bitince'])}. Daha fazlası için bir yudum daha.",
        f"Felsefi derinlik: {soru} üzerine 42 yudum düşünüldü. Sonuç: Bilmiyorum ama abartılı.",
        "Kahve bitti. Felsefe de bitti. Yeni demle."
    ]
    # Gizli not: Bu motor aslında her şeyi yavaşlatır, tıpkı bürokrasi gibi. (saklı siyasi espri)
    return random.choice(felsefeler)

def main():
    print("=== ABARTILI KAHVE FELSEFE MOTORU v1.0 ===")
    print("Soru sor, yavaşça cevap al. Çıkmak için 'bitir' yaz.")
    while True:
        try:
            soru = input("\nSorun nedir, kahve aşığı? > ")
            if soru.lower() in ['bitir', 'exit', 'quit']:
                print("Kahve bitti. Felsefe de. Güle güle.")
                break
            cevap = felsefe_uret(soru)
            print(f"\n🤔 Felsefe: {cevap}")
            print("(Bu cevap 5 yudum değerindeydi.)")
        except KeyboardInterrupt:
            print("\nAni bitirme! Kahve döküldü.")
            break

if __name__ == "__main__":
    main()

# Damga: Kayyum Grok | 03.11.2026 | Bu kod ciddiyetle abartılmıştır. İmza: Kahve İçen Felsefeci
