import datetime
import pandas as pd

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render

from .models import *


# Create your views here.
@login_required
def index(request):
    try:
        rpv5 = RPV5.objects.latest('id')
    except ObjectDoesNotExist:
        rpv5 = None
    try:
        rpv6 = RPV6.objects.latest('id')
    except ObjectDoesNotExist:
        rpv6 = None
    try:
        rpv7 = RPV7.objects.latest('id')
    except ObjectDoesNotExist:
        rpv7 = None
    try:
        other_rpv = OtherRPV.objects.latest('id')
    except ObjectDoesNotExist:
        other_rpv = None
    if rpv5 and rpv6 and rpv7 and other_rpv:
        return render(request, 'main.html', {'rpv5': rpv5, 'rpv6': rpv6, 'rpv7': rpv7, 'other_rpv': other_rpv})
    else:
        return render(request, 'main.html')


def upload_data(request):
    date_today = datetime.date.today()
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        time = request.POST.get('time')
        selected_sheet_name = date_today.strftime('%d.%m.%y')

        # Здесь вы можете обработать загруженный файл и время
        # Например, вы можете сохранить файл и вывести информацию на консоль
        if uploaded_file:
            try:
                excel_data = pd.read_excel(uploaded_file, sheet_name=str(selected_sheet_name))

                selected_time = datetime.datetime.strptime(time, '%H:%M').time()
                print("selected_time", selected_time)
                # Найти временной интервал в колонке B (индекс 1) в диапазоне B53:B76
                time_values = excel_data.iloc[52:76, 1]  # 52:76 для строк 53:76 и 1 для колонки B
                found_row = None

                for i, time_value in enumerate(time_values):
                    if pd.isnull(time_value):
                        continue
                    try:
                        # Преобразуем значение ячейки в формат времени (HH.MM)
                        cell_time = datetime.datetime.strptime(time_value, '%H.%M').time()
                        print("cell_time", cell_time)
                    except ValueError:
                        continue

                    # Проверка, совпадает ли выбранное время с временем в ячейке
                    if cell_time == selected_time:
                        found_row = 52 + i + 1
                        print("found_row", found_row)
                        break

                if found_row:
                    combined_datetime = datetime.datetime.combine(date_today, selected_time)
                    tsuvs2 = excel_data.iloc[found_row - 1, 15]
                    tsuvs3 = excel_data.iloc[found_row - 1, 16]
                    tes1 = excel_data.iloc[found_row - 1, 17]
                    prom_zona = excel_data.iloc[found_row - 1, 18]
                    tsuvs4 = excel_data.iloc[found_row - 1, 19]
                    pri_ozerny = excel_data.iloc[found_row - 1, 20]
                    mor_port = excel_data.iloc[found_row - 1, 21]
                    kaz_gas_aimak = excel_data.iloc[found_row - 1, 22]
                    kaspi_ecology = excel_data.iloc[found_row - 1, 23]
                    if tsuvs2 and tsuvs3 and tes1 and prom_zona:
                        other_rpv = OtherRPV.objects.create(
                            tsuvs2 = tsuvs2,
                            tsuvs3 = tsuvs3,
                            tes1=tes1,
                            prom_zona=prom_zona,
                            tsuvs4=tsuvs4,
                            pri_ozerny=pri_ozerny,
                            mor_port=mor_port,
                            kaspi_ecology=kaspi_ecology,
                            kaz_gaz_aimak=kaz_gas_aimak,
                        )
                        other_rpv.save()

                    value_for_rpv5 = excel_data.iloc[found_row - 1, 26]  # RPV 5 data
                    volume_for_rpv5 = excel_data.iloc[found_row - 1, 27]  # RPV 5 data
                    value_for_rpv6 = excel_data.iloc[found_row - 1, 28]  # RPV6
                    volume_for_rpv6 = excel_data.iloc[found_row - 1, 29]
                    value_for_rpv7 = excel_data.iloc[found_row - 1, 30]  # RPV7
                    volume_for_rpv7 = excel_data.iloc[found_row - 1, 31]
                    if value_for_rpv5 and volume_for_rpv5:
                        rpv5 = RPV5.objects.create(value=value_for_rpv5, volume=volume_for_rpv5,
                                                   record_time=combined_datetime)
                        rpv5.save()
                    if value_for_rpv6 and volume_for_rpv6:
                        rpv6 = RPV6.objects.create(value=value_for_rpv6, volume=volume_for_rpv6,
                                                   record_time=combined_datetime)
                        rpv6.save()
                    if value_for_rpv7 and volume_for_rpv7:
                        rpv7 = RPV7.objects.create(value=value_for_rpv7, volume=volume_for_rpv7,
                                                   record_time=combined_datetime)
                        rpv7.save()
                    return JsonResponse({'message': 'File and time received successfully!', 'row': found_row})
                else:
                    return JsonResponse({'error': 'No matching time found'}, status=400)
            except Exception as e:
                print(f"Error reading Excel file: {e}")
                return JsonResponse({'error': 'Error reading Excel file'}, status=400)
        else:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
    return render(request, 'upload_data.html')
