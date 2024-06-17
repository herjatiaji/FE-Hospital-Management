from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify,
)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

import json
import requests

@app.route("/handle_login", methods=["POST"])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")
    login_data = {"username": username, "password": password}
    
    print("JSON data:", json.dumps(login_data, indent=4))
    
    api_url = "http://127.0.0.1:1330/auth/login"
    response = requests.post(api_url, json=login_data)
    
    if response.status_code == 200:
        session['username'] = username
        login_response = response.json()
        role = login_response.get('role', None)
        session['role']= role
        
        if role == 'Staff Ruangan':
            session['username'] = username
            return redirect('/staff_ruangan') 
        elif role == 'kepala_bidang':
            session['username'] = username
            return redirect('/kepala_bidang')
        elif role == 'Verifikasi':
            session['username'] = username
            return redirect('/verifikasi')
        elif role == 'Staff Gudang':
            session['username'] = username
            return redirect('/staff_gudang')
        elif role  == 'sub_bagian':
            session['username'] = username
            return redirect('/sub_bag')
        
        else:
            flash("Invalid role for dashboard access.", "error")
            return redirect(url_for('login'))
    else:
        flash("Login failed. Please check your username and password.", "error")
        return redirect(url_for('login'))

@app.route("/dashboard")
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("dashboard-staff.html", username=session['username'])


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/")
def index():
    return render_template("login.html", menu="home")


######################################
# Role Sub Bagian / Pejabat Keuangan #
######################################
@app.route("/sub_bag")
def dashboard_subBag():
    return render_template(
        "/pages/sub_bagian/dashboard_kepalaSubBag.html", menu="dashboard"
    )


@app.route("/sub_bag/verif")
def verifikasisubBag():
    data = [
        {
            "no": 1,
            "tanggal": "23/02/2023",
            "ruangan": "Ruangan A",
        },
        {
            "no": 2,
            "tanggal": "25/02/2023",
            "ruangan": "Ruangan B",
        },
        {
            "no": 3,
            "tanggal": "27/02/2023",
            "ruangan": "Ruangan C",
        },
        {
            "no": 4,
            "tanggal": "29/02/2023",
            "ruangan": "Ruangan D",
        },
    ]
    return render_template(
        "/pages/sub_bagian/verifikasi_subBag.html", data=data, menu="verifikasi"
    )


@app.route("/sub_bag/verif/detail")
def verifikasiDetailSubBag():
    return render_template(
        "/pages/sub_bagian/verifikasi-detail-subBag.html", menu="verifikasi"
    )


###################
# Role VERIFIKASI #
###################
@app.route("/verifikasi")
def dashboard_verifikasi():
    return render_template(
        "/pages/verifikasi/dashboard_verifikasi.html", menu="dashboard"
    )


@app.route("/verifikasi/verif")
def verifikasiverif():
    data = [
        {
            "no": 1,
            "tanggal": "23/02/2023",
            "ruangan": "Ruangan A",
        },
        {
            "no": 2,
            "tanggal": "25/02/2023",
            "ruangan": "Ruangan B",
        },
        {
            "no": 3,
            "tanggal": "27/02/2023",
            "ruangan": "Ruangan C",
        },
        {
            "no": 4,
            "tanggal": "29/02/2023",
            "ruangan": "Ruangan D",
        },
    ]
    return render_template(
        "/pages/verifikasi/verifikasi-verifikasi.html", data=data, menu="verifikasi4"
    )


@app.route("/verifikasi/verif/detail")
def verifikasiDetailVerifikasi():
    return render_template(
        "/pages/verifikasi/verifikasi-detail-verifikasi.html", menu="verifikasi4"
    )


########################################
# Role Kepala Bidang / Atasan Langsung #
########################################
@app.route("/kepala_bidang")
def dashboard_kepalaBidang():
    return render_template(
        "/pages/kepala_bidang/dashboard_kepalaBidang.html", menu="dashboard"
    )


@app.route("/kepala_bidang/verif")
def verifikasiKepalaBidang():
    data = [
        {
            "no": 1,
            "tanggal": "23/02/2023",
            "ruangan": "Ruangan A",
        },
        {
            "no": 2,
            "tanggal": "25/02/2023",
            "ruangan": "Ruangan B",
        },
        {
            "no": 3,
            "tanggal": "27/02/2023",
            "ruangan": "Ruangan C",
        },
        {
            "no": 4,
            "tanggal": "29/02/2023",
            "ruangan": "Ruangan D",
        },
    ]
    return render_template(
        "/pages/kepala_bidang/verifikasi-kepalaBidang.html",
        data=data,
        menu="verifikasi5",
    )


@app.route("/kepala_bidang/verif/detail")
def verifikasiDetailkepalaBidang():
    return render_template(
        "/pages/kepala_bidang/verifikasi-detail-kepalaBidang.html", menu="verifikasi5"
    )


################
# Staff Gudang #
################
@app.route("/staff_gudang")
def dashboard_gudang():
    return render_template(
        "/pages/staff_gudang/dashboard_gudang.html", menu="dashboard"
    )


@app.route("/staff_gudang/verif")
def verifikasi_pengajuan():
    data = [
        {
            "no": 1,
            "tanggal": "23/02/2023",
            "ruangan": "Ruangan A",
        },
        {
            "no": 2,
            "tanggal": "25/02/2023",
            "ruangan": "Ruangan B",
        },
        {
            "no": 3,
            "tanggal": "25/02/2023",
            "ruangan": "Ruangan B",
        },
        {
            "no": 4,
            "tanggal": "25/02/2023",
            "ruangan": "Ruangan B",
        },
    ]

    return render_template(
        "/pages/staff_gudang/verifikasi_pengajuan.html",
        data=data,
        menu="verifikasi_pengajuan",
    )


@app.route("/staff_gudang/verif/detail")
def verifikasi_detail_pengajuan():
    return render_template(
        "/pages/staff_gudang/verifikasi-detail-pengajuan.html",
        menu="verifikasi_pengajuan",
    )


@app.route("/staff_gudang/transaksi")
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
    return render_template(
        "/pages/staff_gudang/transaksi_gudang.html", data=data, menu="transaksi_gudang"
    )


@app.route("/staff_gudang/transaksi/detail")
def detail_transaksi_gudang():
    return render_template(
        "/pages/staff_gudang/detail_transaksiGudang.html",
        menu="detail_transaksi_gudang",
    )


#################################
# Role Staff atau Staff Ruangan #
#################################
@app.route("/staff_ruangan")
def dashboardStaff():
    return render_template(
        "/pages/staff_ruangan/dashboard-staff.html", menu="dashboard"
    )


@app.route("/staff_ruangan/stock")
def stock():
    return render_template("/pages/staff_ruangan/stock.html")


@app.route("/staff_ruangan/transaksi")
def transaksi():
    data = [
        {
            "no": 1,
            "tanggal": "23 Februari 2024",
            "status": "Selesai",
            "ruangan": "Ruangan A",
        },
        {
            "no": 2,
            "tanggal": "22 Februari 2024",
            "status": "Proses",
            "ruangan": "Ruangan B",
        },
        {
            "no": 3,
            "tanggal": "24 Februari 2024",
            "status": "Selesai",
            "ruangan": "Ruangan C",
        },
        {
            "no": 4,
            "tanggal": "27 Februari 2024",
            "status": "Selesai",
            "ruangan": "Ruangan B",
        },
        {
            "no": 5,
            "tanggal": "25 Februari 2024",
            "status": "Proses",
            "ruangan": "Ruangan D",
        },
    ]
    return render_template(
        "/pages/staff_ruangan/transaksi.html", data=data, menu="transaksi"
    )


@app.route("/staff_ruangan/transaksi/detail")
def detail_transaksi():
    return render_template("/pages/staff_ruangan/detail_transaksiRuangan.html")


import requests

@app.route("/staff_ruangan/pengajuan")
def pengajuanBarang():
    if request.method == "POST":
        if request.form.get('_method') == 'DELETE':
            return delete_pengajuan_barang(request.form.get('id'))
    api_url = "http://127.0.0.1:1330/staff_ruangan/pengajuan_barang"
    response = requests.get(api_url)
    data = response.json()

   
    pengajuan_barang = data.get('pengajuan_barang', [])

  
    return render_template("/pages/staff_ruangan/pengajuan-barang.html", menu="pengajuan-barang", pengajuan_barang=pengajuan_barang)

@app.route("/staff_ruangan/pengajuan", methods=["POST"])
def sendPengajuanBarang():
    role = session.get('role')
    if request.method == "POST":
        tanggal = request.form.get('tanggal')
        nama_barang = request.form.get('nama_barang')
        jumlah = request.form.get('jumlah')
        ruangan = request.form.get('ruangan')

        data = {
            "role": role,
            "tanggal_pengajuan": tanggal,
            "nama_barang": nama_barang,
            "jumlah": jumlah,
            "ruangan": ruangan
        }

        
        api_url = "http://127.0.0.1:1330/staff_ruangan/pengajuan_barang"
        response = requests.post(api_url, json=data)
        print("JSON data:", json.dumps(data, indent=4))

        if response.status_code == 200:
            flash("Pengajuan barang berhasil diajukan.", "success")
        else:
            flash("Terjadi kesalahan saat mengajukan barang.", "error")

        return redirect(url_for('pengajuanBarang'))
    
@app.route("/staff_ruangan/pengajuan_barang/<string:item_id>", methods=["DELETE"])
def delete_pengajuan_barang(item_id):
    api_url = f"http://127.0.0.1:1330/staff_ruangan/pengajuan_barang/{item_id}"
    response = requests.delete(api_url)
    if response.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": response.text}), response.status_code

@app.route("/staff_ruangan/pengajuan_barang/<string:item_id>", methods=["PUT"])
def update_pengajuan_barang(item_id):
    data = request.get_json()
    api_url = f"http://127.0.0.1:1330/staff_ruangan/pengajuan_barang/{item_id}"
    response = requests.put(api_url, json=data)
    if response.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": response.text}), response.status_code


@app.route("/staff_ruangan/pengusulan")
def pengusulanBarang():
    if request.method == "POST":
        if request.form.get('_method') == 'DELETE':
            return delete_pengajuan_barang(request.form.get('id'))
    api_url = "http://127.0.0.1:1330/staff_ruangan/pengusulan_barang"
    response = requests.get(api_url)
    data = response.json()
    print(data)

   
    pengusulan_barang = data.get('pengusulan_barang', [])
    print(pengusulan_barang)

  
    return render_template("/pages/staff_ruangan/pengusulan_barang.html", menu="pengusulan_barang", pengusulan_barang=pengusulan_barang)

@app.route("/staff_ruangan/pengusulan", methods=["POST"])
def sendPengusulanBarang():
    role = session.get('role')
    if request.method == "POST":
        tanggal = request.form.get('tanggal')
        nama_barang = request.form.get('nama_barang')
        jumlah = request.form.get('jumlah')
        ruangan = request.form.get('ruangan')
        merek = request.form.get('merek')

        data = {
            "role": role,
            "tanggal_pengusulan": tanggal,
            "nama_barang": nama_barang,
            "volume": jumlah,
            "ruangan": ruangan,
            "merek": merek
        }

        
        api_url = "http://127.0.0.1:1330/staff_ruangan/pengusulan_barang"
        response = requests.post(api_url, json=data)
        print("JSON data:", json.dumps(data, indent=4))

        if response.status_code == 200:
            flash("Pengajuan barang berhasil diajukan.", "success")
        else:
            flash("Terjadi kesalahan saat mengajukan barang.", "error")

        return redirect(url_for('pengusulanBarang'))
    
@app.route("/staff_ruangan/pengusulan_barang/<string:item_id>", methods=["DELETE"])
def delete_pengusulan_barang(item_id):
    api_url = f"http://127.0.0.1:1330/staff_ruangan/pengusulan_barang/{item_id}"
    response = requests.delete(api_url)
    if response.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": response.text}), response.status_code
    
@app.route("/staff_ruangan/pengusulan_barang/<string:item_id>", methods=["PUT"])
def update_pengusulan_barang(item_id):
    data = request.get_json()
    api_url = f"http://127.0.0.1:1330/staff_ruangan/pengusulan_barang/{item_id}"
    response = requests.put(api_url, json=data)
    if response.status_code == 200:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": response.text}), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
