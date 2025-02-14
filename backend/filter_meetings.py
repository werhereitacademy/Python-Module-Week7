import pandas as pd
from PyQt6 import QtWidgets
from backend.readfile import read
# 🔹 Evaluation çeviri sözlüğü
evaluation_translation = {
    "VIT projesinin tamamına katılması uygun olur": "It is appropriate to participate in the entire VIT project",
    "VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur": "It is appropriate to receive initial IT training within the VIT project and be directed to ITPH",
    "VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur": "It is appropriate to receive English training within the VIT project and be directed to ITPH",
    "VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur": "It is appropriate to be directly directed to ITPH within the scope of the VIT project",
    "Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur": "It is appropriate to be directed to a job through individual coaching",
    "Bir sonraki VIT projesine katılmak daha uygun olurdu": "It would be more appropriate to participate in the next VIT project",
    "Başka bir sektöre yönlendirilmelidir": "Should be directed to another sector",
    "Diger": "Other",
}


def filter_meetings(ui):
    # ComboBox'tan seçilen Evaluation değerine göre toplantilari filtreler
    selected_english_value = (ui.comboBox.currentText())  # Kullanıcının seçtiği İngilizce değer

    # 🔹 İngilizce değeri Türkçeye çevir
    selected_turkish_value = next((key for key, value in evaluation_translation.items()if value == selected_english_value),None,)

    if selected_turkish_value is None:
        QtWidgets.QMessageBox.warning(None,"Error","No matching Turkish value found for the selected English value.")
        return

    try:
        df = read("Mentor.xlsx")  # Excel'i oku
        df["Evaluation"] = df["Evaluation"].str.strip()  # Boşlukları temizle
        filtered_df = df[df["Evaluation"] == selected_turkish_value]  # Türkçe eşleşeni filtrele

        # TableWidget'ı temizle
        ui.tableWidget.setRowCount(0)

        if filtered_df.empty:
            QtWidgets.QMessageBox.information(None, "Information", "No matching record found.")
            return

        # TableWidget başlıklarını ayarla
        headers = filtered_df.columns.tolist()
        ui.tableWidget.setColumnCount(len(headers))
        ui.tableWidget.setHorizontalHeaderLabels(headers)

        # Verileri ekle
        for row_index, row_data in filtered_df.iterrows():
            row_position = ui.tableWidget.rowCount()  # Mevcut satır sayısını al
            ui.tableWidget.insertRow(row_position)  # Yeni satır ekle
            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                ui.tableWidget.setItem(row_position, col_index, item)

    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Error", f"An error occurred during filtering: {str(e)}")
