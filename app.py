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


# Index Route
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


@app.route("/staff_ruangan/pengajuan")
def pengajuanBarang():
    return render_template(
        "/pages/staff_ruangan/pengajuan-barang.html", menu="pengajuan-barang"
    )


@app.route("/staff_ruangan/pengusulan")
def pengusulanBarang():
    return render_template(
        "/pages/staff_ruangan/pengusulan_barang.html", menu="pengusulan-barang"
    )


if __name__ == "__main__":
    app.run(debug=True)
