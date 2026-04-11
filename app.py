from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql
import requests

app = Flask(__name__)

# Konfigurasi koneksi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'dbpolibatam'
}

def create_connection():
    return pymysql.connect(**db_config)

app.secret_key = "4cc645e832bc2ed0869da6d3a9bdc0ea"

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/tentang', methods=['GET'])
def aboutus():
    return render_template('tentang.html')

@app.route('/joke', methods=['GET'])
def joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke_data = response.json()
    joke_text = joke_data['value']
    return render_template('joke.html', joke=joke_text)

@app.route('/verifikasi-login', methods=['POST'])
def verifikasiLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        cursor.close()

        connection.close()

        if user:
            user_session_data = {
                'id': user[0],
                'email': user[1]
            }
            session['user_id'] = user_session_data['id']
            flash('Login berhasil. Selamat datang!', 'success')
            return redirect('/dashboard')
        else:
            flash('Email atau password salah', 'error')
            return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/mahasiswa', methods=['GET'])
def data_mahasiswa():
    if 'user_id' in session:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT id, nim, nama_lengkap, alamat FROM students ORDER BY id DESC')
        data = cursor.fetchall()
        cursor.close()

        connection.close()

        return render_template('mahasiswa/data-mahasiswa.html', mahasiswa=data)
    else:
        return redirect('/')

@app.route('/mahasiswa/tambah', methods=['GET', 'POST'])
def tambah_mahasiswa():
    if 'user_id' in session:
        if request.method == 'POST':
            nim = request.form['nim']
            nama_lengkap = request.form['nama_lengkap']
            alamat = request.form['alamat']

            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO students (nim, nama_lengkap, alamat) VALUES (%s,%s,%s)",
                           (nim, nama_lengkap, alamat))

            connection.commit()
            cursor.close()
            connection.close()

            flash('Data mahasiswa berhasil ditambahkan!', 'success')
            return redirect(url_for('data_mahasiswa'))
        else:
            return render_template('mahasiswa/tambah-mahasiswa.html')
    else:
        return redirect('/')

@app.route('/mahasiswa/edit/<int:id>', methods=['GET', 'POST'])
def edit_mahasiswa(id):
    if 'user_id' in session:
        if request.method == 'POST':
            nim = request.form['nim']
            nama_lengkap = request.form['nama_lengkap']
            alamat = request.form['alamat']

            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE students
                SET nim = %s, nama_lengkap = %s, alamat = %s
                WHERE id = %s
            """, (nim, nama_lengkap, alamat, id))

            connection.commit()
            cursor.close()
            connection.close()

            flash('Data mahasiswa berhasil diubah!', 'success')
            return redirect(url_for('data_mahasiswa'))
        else:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
            data = cursor.fetchone()
            cursor.close()
            connection.close()

            return render_template('mahasiswa/ubah-mahasiswa.html', mahasiswa=data)
    else:
        return redirect('/')

@app.route('/mahasiswa/delete/<int:id>', methods=['GET'])
def delete_mahasiswa(id):
    if 'user_id' in session:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('DELETE FROM students WHERE id = %s', (id,))

        connection.commit()
        cursor.close()
        connection.close()

        flash('Data mahasiswa berhasil dihapus!', 'success')
        return redirect(url_for('data_mahasiswa'))
    else:
        return redirect('/')

@app.route('/courses', methods=['GET'])
def data_courses():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT course_id, course_name, sks, description FROM courses ORDER BY course_id DESC')
    data = cursor.fetchall()
    cursor.close()

    connection.close()

    return render_template('matakuliah/data-matkul.html', courses=data)

@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form['course_name']
        sks = request.form['sks']
        description = request.form['description']

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO courses (course_name, sks, description) VALUES (%s, %s, %s)",
                    (course_name, sks, description))
        connection.commit()
        cursor.close()
        connection.close()

        flash('Matakuliah berhasil ditambahkan!', 'success')
        return redirect(url_for('data_courses'))
    else:
        return render_template('matakuliah/tambah-matkul.html')

@app.route('/courses/edit/<int:id>', methods=['GET', 'POST'])
def edit_course(id):
    if request.method == 'POST':
        course_name = request.form['course_name']
        sks = request.form['sks']
        description = request.form['description']

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE courses
            SET course_name = %s, sks = %s, description = %s
            WHERE course_id = %s
        """, (course_name, sks, description, id))
        connection.commit()
        cursor.close()
        connection.close()

        flash('Matakuliah berhasil diubah!', 'success')
        return redirect(url_for('data_courses'))
    else:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM courses WHERE course_id = %s", (id,))
        course = cursor.fetchone()
        cursor.close()
        connection.close()

        return render_template('matakuliah/ubah-matkul.html', course=course)

@app.route('/courses/delete/<int:id>', methods=['GET'])
def delete_course(id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM courses WHERE course_id = %s', (id,))
    connection.commit()
    cursor.close()
    connection.close()

    flash('Matakuliah berhasil dihapus!', 'success')
    return redirect(url_for('data_courses'))

if __name__ == "__main__":
    app.run(debug=True, port=9999)
