from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)

@app.route('/login',  methods=['GET'])
def login():
    return render_template('login.html')  


@app.route("/")
def index():
  return render_template('login.html', menu = 'home')

@app.route("/verifikasi-subBag")
def verifikasisubBag():
   data= [{
      "no": 1,
        "tanggal": "23/02/2023",
        "ruangan": "Ruangan A",
    }, {
       "no": 2,
        "tanggal": "25/02/2023",
        "ruangan": "Ruangan B",
    }, {
       "no": 3,
        "tanggal": "27/02/2023",
        "ruangan": "Ruangan C",
    },{
       "no": 4,
        "tanggal": "29/02/2023",
        "ruangan": "Ruangan D",
    }]
   return render_template('verifikasi_subBag.html', data = data, menu = 'verifikasi')

@app.route("/verifikasi-detail-subBag")
def verifikasiDetailSubBag():
  return render_template('verifikasi-detail-subBag.html', menu = 'verifikasi')

@app.route("/dashboard_verifikasi")
def dashboard_verifikasi():
    return render_template('dashboard_verifikasi.html', menu='dashboard')

@app.route("/verifikasi-verifikasi")
def verifikasiverif():
   data= [{
      "no": 1,
        "tanggal": "23/02/2023",
        "ruangan": "Ruangan A",
    }, {
       "no": 2,
        "tanggal": "25/02/2023",
        "ruangan": "Ruangan B",
    }, {
       "no": 3,
        "tanggal": "27/02/2023",
        "ruangan": "Ruangan C",
    },{
       "no": 4,
        "tanggal": "29/02/2023",
        "ruangan": "Ruangan D",
    }]
   return render_template('verifikasi-verifikasi.html', data = data, menu = 'verifikasi4')

@app.route("/verifikasi-detail-verifikasi")
def verifikasiDetailVerifikasi():
  return render_template('verifikasi-detail-verifikasi.html', menu = 'verifikasi4')


@app.route("/dashboard-staff")
def dashboardStaff():
    return render_template('dashboard-staff.html', menu='dashboard')

@app.route("/dashboard_kepalaBidang")
def dashboard_kepalaBidang():
    return render_template('dashboard_kepalaBidang.html', menu='dashboard')

@app.route("/verifikasi-kepalaBidang")
def verifikasiKepalaBidang():
   data= [{
      "no": 1,
        "tanggal": "23/02/2023",
        "ruangan": "Ruangan A",
    }, {
       "no": 2,
        "tanggal": "25/02/2023",
        "ruangan": "Ruangan B",
    }, {
       "no": 3,
        "tanggal": "27/02/2023",
        "ruangan": "Ruangan C",
    },{
       "no": 4,
        "tanggal": "29/02/2023",
        "ruangan": "Ruangan D",
    }]
   return render_template('verifikasi-kepalaBidang.html', data = data, menu = 'verifikasi5')

@app.route("/verifikasi-detail-kepalaBidang")
def verifikasiDetailkepalaBidang():
  return render_template('verifikasi-detail-kepalaBidang.html', menu = 'verifikasi5')


@app.route("/dashboard_gudang")
def dashboard_gudang():
    return render_template('dashboard_gudang.html', menu='dashboard')

@app.route("/verifikasi_pengajuan")
def verifikasi_pengajuan():
    data = [{
      "no": 1,
        "tanggal": "23/02/2023",
        "ruangan": "Ruangan A",
      }, {
       "no": 2,
        "tanggal": "25/02/2023",
        "ruangan": "Ruangan B",
       }, {
       "no": 3,
        "tanggal": "25/02/2023",
        "ruangan": "Ruangan B",

         }, {
       "no": 4,
        "tanggal": "25/02/2023",
        "ruangan": "Ruangan B",
    
    }]
    
    return render_template('verifikasi_pengajuan.html', data = data, menu='verifikasi_pengajuan')

@app.route("/verifikasi-detail-pengajuan")
def verifikasi_detail_pengajuan():
    return render_template('verifikasi-detail-pengajuan.html', menu='verifikasi_pengajuan')

@app.route("/transaksi_gudang")
def transaksiGudang():
    data = [
        {
            "no": 1,
            "tanggal": "23 Februari 2024",
            "status": "Selesai",
            "ruangan": "Gudang A",
        },
        {
            "no": 2,
            "tanggal": "22 Februari 2024",
            "status": "Proses",
            "ruangan": "Gudang B",
        },
        {
            "no": 3,
            "tanggal": "24 Februari 2024",
            "status": "Selesai",
            "ruangan": "Gudang C",
        },
        {
            "no": 4,
            "tanggal": "27 Februari 2024",
            "status": "Selesai",
            "ruangan": "Gudang B",
        },
        {
            "no": 5,
            "tanggal": "25 Februari 2024",
            "status": "Proses",
            "ruangan": "Gudang D",
        },
    ]
    return render_template('transaksi_gudang.html', data=data, menu="transaksi_gudang")

@app.route("/detail_transaksi_gudang")
def detail_transaksi_gudang():
    return render_template('detail_transaksiGudang.html', menu='detail_transaksi_gudang')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route("/transaksi")
def transaksi():
   data = [
      {
      "no":1,
      "tanggal": "23 Februari 2024",
      "status": "Selesai",
      "ruangan": "Ruangan A",
   },
      {
      "no":2,
      "tanggal": "22 Februari 2024",
      "status": "Proses",
      "ruangan": "Ruangan B",
   },
      {
      "no":3,
      "tanggal": "24 Februari 2024",
      "status": "Selesai",
      "ruangan": "Ruangan C",
   },
      {
      "no":4,
      "tanggal": "27 Februari 2024",
      "status": "Selesai",
      "ruangan": "Ruangan B",
   },
      {
      "no":5,
      "tanggal": "25 Februari 2024",
      "status": "Proses",
      "ruangan": "Ruangan D",
   },
   ]
   return render_template('transaksi.html',data=data, menu="transaksi")

@app.route('/detail_transaksiRuangan.html')
def detail_transaksi():
    return render_template('detail_transaksiRuangan.html')

@app.route("/pengajuan-barang")
def pengajuanBarang():
  return render_template('pengajuan-barang.html', menu = 'pengajuan-barang')


@app.route("/pengusulan-barang")
def pengusulanBarang():
    return render_template('pengusulan_barang.html', menu='pengusulan-barang')


if __name__ == "__main__": 
    app.run(debug=True)