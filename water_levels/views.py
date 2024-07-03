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
    try:
        rpvv1 = RPPV1.objects.latest('id')
    except ObjectDoesNotExist:
        rpvv1 = None
    try:
        rpvv2 = RPPV2.objects.latest('id')
    except ObjectDoesNotExist:
        rpvv2 = None
    try:
        brd3 = BRD3.objects.latest('id')
    except ObjectDoesNotExist:
        brd3 = None
    try:
        brd4 = BRD4.objects.latest('id')
    except ObjectDoesNotExist:
        brd4 = None
    if rpv5 and rpv6 and rpv7 and other_rpv:
        return render(request, 'main.html', {'rpv5': rpv5, 'rpv6': rpv6, 'rpv7': rpv7,
                                             'other_rpv': other_rpv, 'rpvv1': rpvv1, 'rpvv2': rpvv2,
                                             'brd3': brd3, 'brd4': brd4 })
    else:
        return render(request, 'main.html')


@login_required
def graphs(request):
    return render(request, 'water_graphs.html')

def upload_data(request):
    date_today = datetime.date.today()
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        time = request.POST.get('time')
        selected_sheet_name = date_today.strftime('%d.%m.%Y')

        # Здесь вы можете обработать загруженный файл и время
        # Например, вы можете сохранить файл и вывести информацию на консоль
        if uploaded_file:
            try:
                excel_data = pd.read_excel(uploaded_file, sheet_name=str(selected_sheet_name))

                selected_time = datetime.datetime.strptime(time, '%H:%M').time()
                print("selected_time", selected_time)
                # Найти временной интервал в колонке B (индекс 1) в диапазоне B53:B76
                time_values = excel_data.iloc[35:59, 1]  # 52:76 для строк 53:76 и 1 для колонки B
                time_values_1 = excel_data.iloc[4:28, 1]
                found_row = None
                found_row_1 = None


                for i, time_value in enumerate(time_values_1):
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
                        found_row_1 = 4 + i + 1
                        print("found_row_1", found_row_1)
                        break

                if found_row_1:
                    combined_datetime = datetime.datetime.combine(date_today, selected_time)
                    rppv_1_level = excel_data.iloc[found_row_1 - 1, 28]
                    rppv_1_volume = excel_data.iloc[found_row_1 - 1, 30]
                    rppv_2_level = excel_data.iloc[found_row_1 - 1, 32]
                    rppv_2_volume = excel_data.iloc[found_row_1 - 1, 34]
                    brd_3_level = excel_data.iloc[found_row_1 - 1, 36]
                    brd_3_volume = excel_data.iloc[found_row_1 - 1, 38]
                    brd_4_level = excel_data.iloc[found_row_1 - 1, 40]

                    temperature_val = excel_data.iloc[found_row_1 - 1, 27]
                    if temperature_val:
                        temperature = Temperature.objects.create(
                            temp=temperature_val,
                            record_time=combined_datetime
                        )
                        temperature.save()


                    dop_poliv = excel_data.iloc[found_row_1 - 1, 17]
                    dop_tceh_left = excel_data.iloc[found_row_1 - 1, 18]
                    dop_tceh_right = excel_data.iloc[found_row_1 - 1, 19]
                    dop_tceh = excel_data.iloc[found_row_1 - 1, 20]
                    dop_cn = excel_data.iloc[found_row_1 - 1, 21]
                    dop_total = excel_data.iloc[found_row_1 - 1, 22]

                    if dop_poliv and dop_tceh_left and dop_tceh_right and dop_tceh and dop_cn and dop_total:
                        dop = DOP.objects.create(
                            poliv=dop_poliv,
                            tceh=dop_tceh,
                            dop_left=dop_tceh_left,
                            dop_right=dop_tceh_right,
                            cn=dop_cn,
                            total=dop_total,
                            record_time=combined_datetime
                        )
                        dop.save()

                    dgo_tec_1 = excel_data.iloc[found_row_1 - 1, 12]
                    dgo_tec_2 = excel_data.iloc[found_row_1 - 1, 13]
                    dgo_tes = excel_data.iloc[found_row_1 - 1, 14]
                    dgo_kaz_azot = excel_data.iloc[found_row_1 - 1, 15]
                    dgo_total = excel_data.iloc[found_row_1 - 1, 16]

                    if dgo_tec_1 and dgo_tec_2 and dgo_tes and dgo_kaz_azot and dgo_total:
                        dgo = DGO.objects.create(
                            tec_1=dgo_tec_1,
                            tec_2=dgo_tec_2,
                            tes_1=dgo_tes,
                            kaz_azot=dgo_kaz_azot,
                            total=dgo_total
                        )
                        dgo.save()

                    brd_4_volume = excel_data.iloc[found_row_1 - 1, 42]
                    if rppv_1_level and rppv_1_volume:
                        rppv_1 = RPPV1.objects.create(level=round(rppv_1_level, 2), volume=round(rppv_1_volume, 2),
                                                   record_time=combined_datetime)
                        rppv_1.save()
                    if rppv_2_level and rppv_2_volume:
                        rppv_2 = RPPV2.objects.create(level=round(rppv_2_level, 2), volume=round(rppv_2_volume, 2),
                                                   record_time=combined_datetime)
                        rppv_2.save()
                    if brd_3_level and brd_3_volume:
                        brd_3 = BRD3.objects.create(level=round(brd_3_level, 2), volume=round(brd_3_volume, 2),
                                                   record_time=combined_datetime)
                        brd_3.save()
                    if brd_4_level and brd_4_level:
                        brd_4 = BRD4.objects.create(level=round(brd_4_level, 2), volume=round(brd_4_volume, 2),
                                                   record_time=combined_datetime)
                        brd_4.save()





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
                        found_row = 35 + i + 1
                        print("found_row", found_row)
                        break

                if found_row:
                    combined_datetime = datetime.datetime.combine(date_today, selected_time)
                    tsuvs2 = excel_data.iloc[found_row - 1, 28]
                    tsuvs3 = excel_data.iloc[found_row - 1, 29]
                    tes1 = excel_data.iloc[found_row - 1, 30]
                    prom_zona = excel_data.iloc[found_row - 1, 31]
                    tsuvs4 = excel_data.iloc[found_row - 1, 32]
                    pri_ozerny = excel_data.iloc[found_row - 1, 33]
                    mor_port = excel_data.iloc[found_row - 1, 34]
                    kaz_gas_aimak = excel_data.iloc[found_row - 1, 35]
                    kaspi_ecology = excel_data.iloc[found_row - 1, 36]
                    sn = excel_data.iloc[found_row - 1, 37]
                    if tsuvs2 and tsuvs3 and tes1 and prom_zona:
                        other_rpv = OtherRPV.objects.create(
                            tsuvs2 = round(tsuvs2),
                            tsuvs3 = round(tsuvs3),
                            tes1=round(tes1),
                            prom_zona=round(prom_zona),
                            tsuvs4=round(tsuvs4),
                            pri_ozerny=round(pri_ozerny),
                            mor_port=round(mor_port),
                            kaspi_ecology=round(kaspi_ecology),
                            kaz_gaz_aimak=round(kaz_gas_aimak),
                            sn=round(sn),
                        )
                        other_rpv.save()
                    output_water = excel_data.iloc[found_row - 1, 38]
                    input_water = excel_data.iloc[found_row - 1, 5]
                    input_output_id = None
                    if output_water and input_water:
                        input_output = InputOutputWater.objects.create(input_water=input_water,
                                                                       output_water=output_water,
                                                                       record_time=combined_datetime)
                        input_output_id = input_output.id
                        input_output.save()



                    value_for_rpv5 = excel_data.iloc[found_row - 1, 6]  # RPV 5 data
                    volume_for_rpv5 = excel_data.iloc[found_row - 1, 8]  # RPV 5 data
                    value_for_rpv6 = excel_data.iloc[found_row - 1, 10]  # RPV6
                    volume_for_rpv6 = excel_data.iloc[found_row - 1, 12]
                    value_for_rpv7 = excel_data.iloc[found_row - 1, 14]  # RPV7
                    volume_for_rpv7 = excel_data.iloc[found_row - 1, 16]
                    if value_for_rpv5 and volume_for_rpv5:
                        rpv5 = RPV5.objects.create(value=round(value_for_rpv5, 2), volume=round(volume_for_rpv5, 2),
                                                   record_time=combined_datetime, input_output_water=input_output_id)
                        rpv5.save()
                    if value_for_rpv6 and volume_for_rpv6:
                        rpv6 = RPV6.objects.create(value=round(value_for_rpv6, 2), volume=round(volume_for_rpv6, 2),
                                                   record_time=combined_datetime, input_output_water=input_output_id)
                        rpv6.save()
                    if value_for_rpv7 and volume_for_rpv7:
                        rpv7 = RPV7.objects.create(value=round(value_for_rpv7, 2), volume=round(volume_for_rpv7, 2),
                                                   record_time=combined_datetime, input_output_water=input_output_id)
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
