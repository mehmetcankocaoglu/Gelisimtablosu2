import ipaddress

print("=== ROTA ÖZETLEME (ROUTE SUMMARIZATION) HESAPLAYICI ===")

# İstenirse input ile alınabilir, senaryoya uygun olması için varsayılan değerler atandı.
start_input = input("Başlangıç alt ağını girin (Örnek: 172.16.16.0/24): ") or "172.16.16.0/24"
end_input = input("Bitiş alt ağını girin (Örnek: 172.16.31.0/24): ") or "172.16.31.0/24"

try:
    # Başlangıç ve bitiş ağlarını tanımla
    start_net = ipaddress.IPv4Network(start_input)
    end_net = ipaddress.IPv4Network(end_input)

    # Başlangıç ağının ilk IP'sinden, bitiş ağının son IP'sine (Broadcast) kadar olan aralığı bul
    # summarize_address_range fonksiyonu bu aralığı en az sayıda CIDR bloğu ile özetler.
    summary_routes = list(ipaddress.summarize_address_range(start_net.network_address, end_net.broadcast_address))

    print("\n=== ÖZET ROTA BİLGİLERİ ===")
    
    if len(summary_routes) == 1:
        net = summary_routes[0]
        print("✅ Başarılı! Verilen aralık tek bir özet rota ile ifade edilebilir.")
        print(f"Özet Rota (Supernet):  {net}")
        print(f"Yeni Subnet Maskesi:   {net.netmask}")
        print(f"Kapsadığı Host Sayısı: {net.num_addresses}")
        print(f"İlk IP Adresi:         {net.network_address}")
        print(f"Broadcast Adresi:      {net.broadcast_address}")
    else:
        print("⚠️ Uyarı: Bu IP aralığı tek bir CIDR bloğuna tam uymuyor. Birden fazla kural gerektirir:")
        for route in summary_routes:
            print(f"👉 {route}")

except ValueError as e:
    print(f"❌ Hatalı IP adresi veya formatı girdin! Detay: {e}")
