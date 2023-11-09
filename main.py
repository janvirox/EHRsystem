from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    try:
        with open(fileName, 'r') as file:
            for line in file:
                line = line.strip()
                fields = line.split(',')
                if len(fields) != 8:
                    print(f"Invalid number of fields ({len(fields)}) in line: {line}")
                else:
                    continue

                try:
                    patientId = int(fields[0])
                    date = str(fields[1])
                    temperature = float(fields[2])
                    heartRate = int(fields[3])
                    respiratoryRate = int(fields[4])
                    sbp = int(fields[5])
                    dbp = int(fields[6])
                    spo2 = int(fields[7])
                except ValueError:
                    print(f"Invalid data type in line: {line}")
                    continue

                if temperature < 35 or temperature > 42:
                    print(f"Invalid temperature value ({temperature}) in line: {line}")
                    continue

                if heartRate < 30 or heartRate > 180:
                    print(f"Invalid heart rate value ({heartRate}) in line: {line}")
                    continue

                if respiratoryRate < 5 or respiratoryRate > 40:
                    print(f"Invalid respiratory rate value ({respiratoryRate}) in line: {line}")
                    continue

                if sbp < 70 or sbp > 200:
                    print(f"Invalid systolic blood pressure value ({sbp}) in line: {line}")
                    continue

                if dbp < 40 or dbp > 120:
                    print(f"Invalid diastolic blood pressure value ({dbp}) in line: {line}")
                    continue

                if spo2 < 70 or spo2 > 100:
                    print(f"Invalid oxygen saturation value ({spo2}) in line: {line}")
                    continue

                visit = [date, temperature, heartRate, respiratoryRate, sbp, dbp, spo2]
                if patientId not in patients:
                    patients[patientId] = []
                patients[patientId].append(visit)
        return patients
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        # raise  # uncomment to re-raise the exception if desired
    return patients

def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    if patientId == 0:
        for patientId, patientData in patients.items():
            print("Patient ID:", patientId)
            for visit in patientData:
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % visit[1], "C")
                print("  Heart Rate:", visit[2], "bpm")
                print("  Respiratory Rate:", visit[3], "bpm")
                print("  Systolic Blood Pressure:", visit[4], "mmHg")
                print("  Diastolic Blood Pressure:", visit[5], "mmHg")
                print("  Oxygen Saturation:", visit[6], "%")
    else:
        if not isinstance(patientId, int) or patientId < 0:
            print("Error: patientId should be a non-negative integer")
            return
        if patientId not in patients:
            print(f"Patient with ID {patientId} not found.")
            return
        patient_data = patients[patientId]
        print("Patient ID:", patientId)
        for visit in patient_data:
            print(" Visit Date:", visit[0])
            print("  Temperature:", "%.2f" % visit[1], "C")
            print("  Heart Rate:", visit[2], "bpm")
            print("  Respiratory Rate:", visit[3], "bpm")
            print("  Systolic Blood Pressure:", visit[4], "mmHg")
            print("  Diastolic Blood Pressure:", visit[5], "mmHg")
            print("  Oxygen Saturation:", visit[6], "%")

# def displayPatientData(patients, patientId=0):
#     """
#     Displays patient data for a given patient ID.
#
#     patients: A dictionary of patient dictionaries, where each patient has a list of visits.
#     patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
#     """
#     #######################
#     patients = {}
#     for line in patients:
#             line = line.strip()
#             fields = line.split(',')
#             if len(fields) != 8:
#                 print(f"Invalid number of fields ({len(fields)}) in line: {line}")
#             else:
#                 continue
#
#             try:
#                 patientId = int(fields[0])
#                 date = str(fields[1])
#                 temperature = float(fields[2])
#                 heartRate = int(fields[3])
#                 respiratoryRate = int(fields[4])
#                 sbp = int(fields[5])
#                 dbp = int(fields[6])
#                 spo2 = int(fields[7])
#             except ValueError:
#                 print(f"Invalid data type in line: {line}")
#                 continue
#     #patientId = int(patients[0])
#     if patientId == 0:
#         for patientId, patientData in patients.items():
#             print("Patient ID:", patientId)
#             for visit in patientData:
#                 print(" Visit Date:", visit[0])
#                 print("  Temperature:", "%.2f" % visit[1], "C")
#                 print("  Heart Rate:", visit[2], "bpm")
#                 print("  Respiratory Rate:", visit[3], "bpm")
#                 print("  Systolic Blood Pressure:", visit[4], "mmHg")
#                 print("  Diastolic Blood Pressure:", visit[5], "mmHg")
#                 print("  Oxygen Saturation:", visit[6], "%")
#     else:
#         if not isinstance(patientId, int) or patientId < 0:
#             print("Error: patientId should be a non-negative integer")
#             return
#     if patientId not in patients:
#         print(f"Patient with ID {patientId} not found.")
#         return
#     patient_data = patients[patientId]
#     print("Patient ID:", patientId)
#     for visit in patient_data:
#         print(" Visit Date:", visit[0])
#         print("  Temperature:", "%.2f" % visit[1], "C")
#         print("  Heart Rate:", visit[2], "bpm")
#         print("  Respiratory Rate:", visit[3], "bpm")
#         print("  Systolic Blood Pressure:", visit[4], "mmHg")
#         print("  Diastolic Blood Pressure:", visit[5], "mmHg")
#         print("  Oxygen Saturation:", visit[6], "%")


##########

def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    # Check if patients is a dictionary

    if patientId == 0:
        # Display vital signs for all patients
        temp_total = 0
        hr_total = 0
        rr_total = 0
        sbp_total = 0
        dbp_total = 0
        spo2_total = 0
        num_patients = 0

        for patientId, visits in patients.items():
            for visit in visits:
                temp_total += visit['temp']
                hr_total += visit['hr']
                rr_total += visit['rr']
                sbp_total += visit['sbp']
                dbp_total += visit['dbp']
                spo2_total += visit['spo2']
            num_visits = len(visits)
            num_patients += 1

        if num_patients > 0:
            avg_temp = temp_total / (num_patients * num_visits)
            avg_hr = hr_total / (num_patients * num_visits)
            avg_rr = rr_total / (num_patients * num_visits)
            avg_sbp = sbp_total / (num_patients * num_visits)
            avg_dbp = dbp_total / (num_patients * num_visits)
            avg_spo2 = spo2_total / (num_patients * num_visits)

            print("Average vital signs for all patients:")
            print("  Temperature:", "%.2f" % avg_temp, "C")
            print("  Heart Rate:", "%.2f" % avg_hr, "bpm")
            print("  Respiratory Rate:", "%.2f" % avg_rr, "bpm")
            print("  Systolic Blood Pressure:", "%.2f" % avg_sbp, "mmHg")
            print("  Diastolic Blood Pressure:", "%.2f" % avg_dbp, "mmHg")
            print("  Oxygen Saturation:", "%.2f" % avg_spo2, "%")
        else:
            print("No patient data found.")

    else:
        # Display vital signs for the specified patient
        if patientId in patients:
            visits = patients[patientId]
            temp_total = 0
            hr_total = 0
            rr_total = 0
            sbp_total = 0
            dbp_total = 0
            spo2_total = 0
            num_visits = len(visits)

            for visit in visits:
                temp_total += visit['temp']
                hr_total += visit['hr']
                rr_total += visit['rr']
                sbp_total += visit['sbp']
                dbp_total += visit['dbp']
                spo2_total += visit['spo2']

            if num_visits > 0:
                avg_temp = temp_total / num_visits
                avg_hr = hr_total / num_visits
                avg_rr = rr_total / num_visits
                avg_sbp = sbp_total / num_visits
                avg_dbp = dbp_total / num_visits
                avg_spo2 = spo2_total / num_visits

                print("Vital Signs for Patient {}:".format(patientId))
                print("  Average temperature:", "{:.2f}".format(avg_temp), "C")
                print("  Average heart rate:", "{:.2f}".format(avg_hr), "bpm")
                print("  Average respiratory rate:", "{:.2f}".format(avg_rr), "bpm")
                print("  Average systolic blood pressure:", "{:.2f}".format(avg_sbp), "mmHg")
                print("  Average diastolic blood pressure:", "{:.2f}".format(avg_dbp), "mmHg")
                print("  Average oxygen saturation:", "{:.2f}".format(avg_spo2), "%")




    #######################



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    #######################
    '''
    # check for input errors
    try:
        # check date format
        datetime.datetime.strptime(date, '%Y-%m-%d')
        # check date validity
        year, month, day = map(int, date.split('-'))
        datetime.date(year, month, day)
    except ValueError:
        print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
        return

    if not (35.0 <= temp <= 42.0):
        print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        return

    if not (30 <= hr <= 180):
        print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        return

    if not (5 <= rr <= 40):
        print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        return

    if not (70 <= sbp <= 200):
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        return

    if not (40 <= dbp <= 120):
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        return

    if not (70 <= spo2 <= 100):
        print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
        return

    # add visit to patients dictionary
    if patientId in patients:
        patients[patientId].append({'date': date, 'temperature': temp, 'heart_rate': hr,
                                    'respiratory_rate': rr, 'systolic_blood_pressure': sbp,
                                    'diastolic_blood_pressure': dbp, 'oxygen_saturation': spo2})
    else:
        patients[patientId] = [{'date': date, 'temperature': temp, 'heart_rate': hr,
                                    'respiratory_rate': rr, 'systolic_blood_pressure': sbp,
                                    'diastolic_blood_pressure': dbp, 'oxygen_saturation': spo2}]

    # add visit to file
    with open(readPatientsFromFile(), 'a') as f:
        f.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")

    print(f"Visit is saved successfully for Patient #{patientId}")
'''
    #######################



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    #######################
    ####
    for patientId, patientVisits in patients.items():
        for visit in patientVisits:
            date = visit[0]
            try:
                visit_year, visit_month, visit_day = [int(x) for x in date.split("-")]
            except ValueError:
                # ignore visits with invalid date information
                continue
            if year is not None and year != visit_year:
                continue
            if month is not None and month != visit_month:
                continue
            visits.append((patientId, visit))
    return visits

    #######################



def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #######################
    for patient_id, visits in patients.items():
        for visit in visits:
            heart_rate = visit[2]
            systolic_bp = visit[4]
            diastolic_bp = visit[5]
            oxygen_sat = visit[6]
            if heart_rate > 100 or heart_rate < 60 or systolic_bp > 140 or diastolic_bp > 90 or oxygen_sat < 90:
                followup_patients.append(patient_id)
                break
    #######################
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #######################
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}")
        return

        # Remove all visits for the given patientId
    del patients[patientId]

    # Write remaining patient data back to the file
    with open(filename, 'w') as f:
        for pid, visits in patients.items():
            for visit in visits:
                f.write(
                    f"{pid},{visit['date']},{visit['temp']},{visit['hr']},{visit['rr']},{visit['sbp']},{visit['dbp']},{visit['spo2']}\n")

    print(f"Data for patient {patientId} has been deleted.")
    #######################




###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = (input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = (input("Enter patient ID (or '0' for all patients): "))
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
