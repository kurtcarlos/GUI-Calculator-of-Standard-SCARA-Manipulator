## SCARA RRP Manipulator Design Calculator - Forward Kinematics

import numpy as np
import math
import PySimpleGUI as sg
import pandas as pd

# GUI code

sg.theme('LightPurple')

# Excel read code

EXCEL_FILE = 'SCARA_RRP_FK.xlsx'
df = pd.read_excel(EXCEL_FILE)

# Lay-out code

Main_layout = [
    [sg.Push()],
    
    [sg.Push(), sg.Text('SCARA RRP Manipulator MEXE Calculator', font = ("Impact", 22)), sg.Push()],
    
    [sg.Push()],
    [sg.Push()],
    [sg.Push()],
    
    [sg.Push(), sg.Button('CLICK THIS FIRST TO GENERATE CALCULATOR!', font = ("Arial Black", 11), size=(45,0), button_color=('black', '#bdad99')), sg.Push()],
    [sg.Push()],
    [sg.Push()],
    [sg.Push()],
    [sg.Push()],
    
    [sg.Text('Please fill out the following fields:', font = ("Copperplate Gothic Light", 9))],
    [sg.Push()],
    
    [sg.Text('a1 = ', font = ('Cambria', 10)),sg.InputText('40', key='a1', size=(13,10)), 
     sg.Text ('mm', font = ("Century Gothic", 8)), sg.Push(),
     sg.Text('T1 = ', font = ('Cambria', 10)),sg.InputText('0', key='T1', size=(13,10)),
     sg.Text ('degrees', font = ("Century Gothic", 8)),
     sg.Push(), sg.Button('Jacobian Matrix (J)', disabled=True, font = ('Copperplate Gothic Light', 8), size = (24,), button_color=('black', '#d1c7ba')),
     sg.Button('Determinant (J)', disabled=True, font = ('Copperplate Gothic Light', 8), size = (24,1), button_color=('black', '#d1c7ba')), sg.Push()],
    
    [sg.Push()],
    [sg.Push()],
    
    [sg.Text('a2 = ', font = ('Cambria', 10)),sg.InputText('30', key='a2', size=(13,10)),
     sg.Text ('mm', font = ("Century Gothic", 8)), sg.Push(),
     sg.Text('T2 = ', font = ('Cambria', 10)),sg.InputText('0', key='T2', size=(13,10)),
     sg.Text ('degrees', font = ("Century Gothic", 8)),
     sg.Push(), sg.Button('Inverse of J', disabled=True, font = ('Copperplate Gothic Light', 8), size = (24,1), button_color=('black', '#d1c7ba')),
     sg.Button('Transpose of J', disabled=True, font = ('Copperplate Gothic Light', 8), size = (24,1), button_color=('black', '#d1c7ba')), sg.Push()],
    
    [sg.Push()],
    
    [sg.Text('a3 = ', font = ('Cambria', 10)),sg.InputText('70', key='a3', size=(13,10)),
     sg.Text ('mm', font = ("Century Gothic", 8)), sg.Push(),
     sg.Text('d3 = ', font = ('Cambria', 10)),sg.InputText('0', key='d3', size=(13,10)),
     sg.Text ('mm', font = ("Century Gothic", 8)),
     sg.Push(),sg.Button('Path and Trajectory Planning', disabled=True, font = ('Copperplate Gothic Light', 8), size=(48,2), button_color=('black', '#d1c7ba')), sg.Push()],
   
    [sg.Text('a4 = ', font = ('Cambria', 10)),sg.InputText('50', key='a4', size=(13,10)),
     sg.Text ('mm', font = ("Century Gothic", 8))], 
    
    [sg.Push()],
  
    [sg.Text('a5 = ', font = ('Cambria', 10)),sg.InputText('30', key='a5', size=(13,10)),
    sg.Text ('mm', font = ("Century Gothic", 8))],
  
    [sg.Push()],
    
    [sg.Push(), sg.Button('Solve Forward Kinematics', disabled=True, tooltip = 'Click the TOP button first to generate calculator!', font = ('Arial Black', 10), size=(37,0), button_color=('black', '#bdad99')),
    sg.Push(),sg.Button('Solve Inverse Kinematics', disabled=True, font = ("Arial Black", 10), size=(38,0), button_color=('#362706', '#bdad99')), sg.Push()],
    [sg.Push()],
    
    [sg.Frame('Position Vector: ',[[
        sg.Text('X = ', font = ('Cambria', 10)),sg.InputText(key='X', size =(10,1)),
        sg.Text ('mm', font = ("Century Gothic", 8)),
        sg.Text('Y = ', font = ('Cambria', 10)),sg.InputText(key='Y', size =(10,1)),
        sg.Text ('mm', font = ("Century Gothic", 8)),
        sg.Text('Z = ', font = ('Cambria', 10)),sg.InputText(key='Z', size =(10,1)), 
        sg.Text ('mm', font = ("Century Gothic", 8))]], font = ('Copperplate Gothic Light', 10))],
    
    [sg.Frame('H0_3 Transformation Matrix & Position Vectors = ',[[sg.Output(size=(56,15))]]),
     sg.Push(), sg.Image('Untitled design (2).png')],

    [sg.Submit(font = ('Century Gothic', 8), button_color=('black', '#E9E5D6')), sg.Exit(font = ('Century Gothic', 8), button_color=('black', '#E9E5D6'))]
]

# Window Code
window = sg.Window('SCARA RRP Manipulator MEXE Calculator', Main_layout, resizable=True)

# Inverse Kinematics Window function

def Inverse_Kinematics_window():
    sg.theme('LightPurple')
    
    EXCEL_FILE = 'SCARA_RRP_IK.xlsx'
    IK_df = pd.read_excel(EXCEL_FILE)
    
    IK_layout = [
    [sg.Push(),sg.Text ('Inverse Kinematics', font = ("Impact", 17)), sg.Push()],
    
    [sg.Push()],
    [sg.Push()],
    [sg.Push()],
    
    [sg.Text ('Fill out the following fields:', font = ("Copperplate Gothic Light", 9))],
    
    [sg.Push()],
    
    [sg.Text('a1 = ', font = ("Cambria", 10)),sg.InputText('40', key='a1', size=(10,10)),
     sg.Text('mm', font = ("Century Gothic", 8)), 
     sg.Text('X = ', font = ("Cambria", 10)),sg.InputText('0', key='X', size=(10,10)),
     sg. Text('mm', font = ("Century Gothic", 8))],
                  
    [sg.Text('a2 = ', font = ("Cambria", 10)),sg.InputText('30', key='a2', size=(10,10)),
     sg.Text ('mm', font = ("Century Gothic", 8)),
     sg.Text('Y = ', font = ("Cambria", 10)),sg.InputText('0',key='Y', size=(10,10)),
     sg.Text('mm', font = ("Century Gothic", 8))],
        
    [sg.Text('a3 = ', font = ("Cambria", 10)),sg.InputText('70', key='a3', size=(10,10)),
     sg.Text ('mm', font = ("Century Gothic", 8)),
     sg.Text('Z = ', font = ("Cambria", 10)),sg.InputText('0',key='Z', size=(10,10)),
     sg.Text ('mm', font = ("Century Gothic", 8))],
        
    [sg.Text('a4 = ', font = ("Cambria", 10)),sg.InputText('50', key='a4', size=(10,10)),
     sg.Text ('mm', font = ("Century Gothic", 8))],
        
    [sg.Text('a5 = ', font = ("Cambria", 10)),sg.InputText('30', key='a5', size=(10,10)),
     sg.Text('mm', font = ("Century Gothic", 8))],
    
    [sg.Push()],
    [sg.Push()],
    [sg.Push()],
    
    [sg.Button('Solve Inverse Kinematics', font = ("Arial Black", 10), button_color=('black', '#bdad99')), sg.Push()],
    
    [sg.Push()],
    [sg.Push()],
    
    [sg.Frame('Position Vector: ',[[
        sg.Text('Th1 = ', font = ("Cambria", 10)),sg.InputText(key='IK_Th1', size=(10,1)),
        sg.Text('degrees', font = ("Century Gothic", 8)),
        sg.Text('Th2 = ', font = ("Cambria", 10)) ,sg.InputText(key='IK_Th2', size=(10,1)),
        sg.Text('degrees', font = ("Century Gothic", 8)),
        sg.Text( 'd3 = ', font = ("Cambria", 10)),sg.InputText(key='IK_d3', size=(10,1)),
        sg.Text('mm', font = ("Century Gothic", 8)),]])],
    
    [sg.Push()],
    [sg.Push()],
    [sg.Push()],
    
    [sg.Submit(font = ("Century Gothic", 10)),sg.Exit(font = ("Century Gothic", 10))]  
    ]
           
    # Window Code
    Inverse_Kinematics_window = sg.Window('Inverse Kinematics', IK_layout)
    
    while True:
        event, values = Inverse_Kinematics_window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    
        elif event == 'Solve Inverse Kinematics':
            # Link Lengths
            a1 = float (values['a1']) # 40 mm
            a2 = float (values['a2']) # 30 mm
            a3 = float (values['a3']) # 70 mm
            a4 = float (values['a4']) # 50 mm
            a5 = float (values['a5']) # 30 mm
            
            # Position Vectors
            X = float (values['X'])
            Y = float (values['Y'])
            Z = float (values['Z'])
        
            try:
                phi2 = np.arctan(Y0_3/X0_3)
            except:
                phi2 = -1 #NAN
                sg.popup ('Warning! Present values cause error.')
                sg.popup ('Restart the GUI then assign proper values!')
                break
        
            # Inverse Kinematics
            
            #Th2
            phi2 = (np.arctan(Y0_3/X0_3))*180.0/np.pi
            r1 = math.sqrt((Y0_3**2)+(X0_3**2))
            phi1 = (np.arccos((a4**2-r1**2-a2**2)/(-2.0*r1*a2)))*180.0/np.pi
            Th1 = (phi2)-(phi1)
            phi3 = (np.arccos((r1**2-a2**2-a4**2)/(-2.0*a2*a4)))*180.0/np.pi
            Th2 = 180 - phi3
            d3 = (a1)+(a3)-(a5)-(Z0_3)
                  
            #print("Th1 = ", np.around(Th1,3))
            #print("Th2 = ", np.around(Th2,3))
            #print("d3 = ", np.around(d3,3))
                
            Th1 = Inverse_Kinematics_window['IK_Th1'].Update (np.around(Th1,3))
            Th2 = Inverse_Kinematics_window['IK_Th2'].Update(np.around(Th2,3))
            d3 = Inverse_Kinematics_window['IK_d3'].Update(np.around(d3,3))
    
        elif event == 'Submit':
            IK_df = IK_df.append (values, ignore_index=True)
            IK_df.to_excel(EXCEL_FILE, index=False)
            sg.popup ('Your data has been successfully saved!')
              
    Inverse_Kinematics_window.close()
          
# Variable Codes for disabling buttons
disable_FK = window['Solve Forward Kinematics']
disable_J = window['Jacobian Matrix (J)']
disable_DetJ = window['Determinant (J)']
disable_IV = window['Inverse of J']
disable_TJ = window['Transpose of J']
disable_IK = window['Solve Inverse Kinematics']
disable_PT = window['Path and Trajectory Planning']


while True:
    event,values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
        
    elif event == 'CLICK THIS FIRST TO GENERATE CALCULATOR!':
        disable_FK.update(disabled=False)
        disable_J.update(disabled=True)
        disable_DetJ.update(disabled=True)
        disable_IV.update(disabled=True)
        disable_TJ.update(disabled=True)
        disable_IK.update(disabled=False)
        disable_PT.update(disabled=True)
        
    elif event == 'Solve Forward Kinematics':
        # Forward Kinematic Codes
        a1 = values['a1']
        a2 = values['a2']
        a3 = values['a3']
        a4 = values['a4']
        a5 = values['a5']
        
        T1 = values['T1']
        T2 = values['T2']
        d3 = values['d3']
        
        T1 = (float(T1)/180.0)*np.pi # Theta 1 in radians
        T2 = (float(T2)/180.0)*np.pi # Theta 2 in radians
        
        PT = [[(float(T1)),(0.0/180.0)*np.pi,float(a2),float(a1)],
              [(float(T2)),(180.0/180.0)*np.pi,float(a4),float(a3)],
              [(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,float(a5)+float(d3)]]
        
        i = 0
        H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
                [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
                [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
                [0,0,0,1]]
        i = 1
        H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
                [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
                [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
                [0,0,0,1]]
        i = 2
        H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
                [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
                [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
                [0,0,0,1]]
                                                                 
        H0_1 = np.matrix(H0_1)
        #print("H0_1=")
        #print(H0_1)
        
        H1_2 = np.matrix(H1_2)
        #print("H1_2=")
        #print(H1_2)
        
        H2_3 = np.matrix(H2_3)
        #print("H2_3=")
        #print(H2_3)
        
        H0_2 = np.dot(H0_1,H1_2)
        #print("H0_2=")
        #print(np.matrix(H0_2))
        
        H0_3 = np.dot(H0_2,H2_3)
        print("H0_3=")
        print(np.matrix(H0_3))
        
        # Position Vectors X Y Z
        X0_3 = H0_3[0,3]
        print("X = ", X0_3)
        
        Y0_3 = H0_3[1,3]
        print("Y = ", Y0_3)
        
        Z0_3 = H0_3[2,3]
        print("Z= ", Z0_3)

        disable_J.update(disabled=False)
        disable_PT.update(disabled=False)
        
    elif event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Your data has been successfully saved!')

    elif event == 'Jacobian Matrix (J)':
        ### Jacobian Matrix
        ## 1. Linear/Prismatic Vectors
        Z_1 = [[0],[0],[1]]

        # Rows 1-3, Column 1
        J1a = [[1,0,0],[0,1,0],[0,0,1]]
        J1a = np.dot(J1a,Z_1)

        try:
            H0_3 = np.matrix(H0_3)
        except:
            H0_3 = -1 #NAN
            sg.popup('Warning! The TOP button was not pressed.')
            sg.popup('Restart the GUI and click the TOP button to generate calculator!')
            break

        J1b_1 = H0_3[0:3,3:] 
        #print("J1b_1 = ")
        #print(np.matrix(J1b_1))

        J1b_2 = [[0],[0],[0]]
        #print(np.matrix(J1b_2))

        J1b = J1b_1 - J1b_2
        #print('J1b = ')
        #print(np.matrix(J1b))

        J1 = [[(J1a[1,0]*J1b[2,0])-(J1a[2,0]*J1b[1,0])],
              [(J1a[2,0]*J1b[0,0])-(J1a[0,0]*J1b[2,0])],
              [(J1a[0,0]*J1b[1,0])-(J1a[1,0]*J1b[0,0])]]
        #print('J1 = ')
        #print(np.matrix(J1))
        
        # Rows 1-3, Column 2
        try:
            H0_1 = np.matrix(H0_1)
        except:
            H0_1 = -1 #NAN
            sg.popup('Warning! The TOP button was not pressed!')
            sg.popup('Restart the GUI and click the TOP button to generate calculator!')
            break
        
        J2a = H0_1[0:3,0:3]
        J2a = np.dot(J2a,Z_1)
        #print("J2a = ")
        #print(J2a)

        J2b_1 = H0_3[0:3,3:]
        J2b_1 = np.matrix(J2b_1)
        #print("J2b_1 = ")
        #print(J2b_1)

        J2b_2 = H0_1[0:3,3:]
        J2b_2 = np.matrix(J2b_2)
        #print("J2b_2 = ")
        #print(J2b_2)

        J2b = J2b_1 - J2b_2
        #print("J2b = ")
        #print(J2b)

        J2 = [[(J2a[1,0]*J2b[2,0])-(J2a[2,0]*J2b[1,0])],
              [(J2a[2,0]*J2b[0,0])-(J2a[0,0]*J2b[2,0])],
              [(J2a[0,0]*J2b[1,0])-(J2a[1,0]*J2b[0,0])]]
        #print("J2 = ")
        #print(np.matrix(J2))
        
        # Rows 1-3, Column 3
        J3 = [[1,0,0],[0,-1,0],[0,0,-1]]
        J3 = np.dot(J3,Z_1)
        J3 = np.matrix(J3)
        #print('J3 = ')
        #print(np.matrix(J3))
        
        ## 2. Rotation/Orientation Vectors
        J4 = [[0],[0],[1]]
        J4 = np.matrix(J4)
        #print("J4 = ")
        #print(J4)

        J5 = H0_1[0:3,0:3]
        J5 = np.dot(J5,Z_1)
        J5 = np.matrix(J5)
        #print("J5 = ")
        #print(J5)

        J6 = [[0],[0],[0]]
        J6 = np.matrix(J6)
        #print("J6 = ")
        #print(J6)
         
        ## 3. Concatenated Jacobian Matrix
        JM1 = np.concatenate((J1,J2,J3),1)
        JM2 = np.concatenate((J4,J5,J6),1)
    

        J = np.concatenate((JM1,JM2),0)
        #print("J = ")
        #print(J)
        
        sg.popup('J = ', J)
        
        DJ = np.linalg.det(JM1)
        if 0.0 >= DJ > -1.0:
            disable_IV.update(disabled=True)
            sg.popup('Jacobian Matrix is Non-Invertible')

        elif DJ != 0.0 or DJ != -0.0:
            disable_IV.update(disabled=False)
        
        
        disable_J.update(disabled=True)
        disable_DetJ.update(disabled=False)
        disable_TJ.update(disabled=False)
        
    elif event == 'Determinant (J)':
        # singularity = Det(J)
        # np.linalg.det(M)
        # Let JM1 become the 3x3 position matrix for obtaining the determinant
        
        try:
            JM1 = np.concatenate((J1,J2,J3),1)
        except:
            JM1 = -1 #NAN
            sg.popup('Warning! The TOP button was not pressed!')
            sg.popup('Restart the GUI and click the TOP button to generate calculator!')
            break
            
        DJ = np.linalg.det(JM1)
        #print('Determinant of J = ', DJ)
        sg.popup('Determinant of J = ', DJ)
        
        if 0.0 >= DJ > -1.0:
            disable_IV.update(disabled=True)
            sg.popup('Jacobian Matrix is Non-Invertible')
            
    elif event == 'Inverse of J':
        # Inv(J)
        
        try:
            JM1 = np.concatenate((J1,J2,J3),1)
        except:
            JM1 = -1 #NAN
            sg.popup('Warning! The TOP button was not pressed!')
            sg.popup('Restart the GUI and click the TOP button to generate calculator!')
            break
            
        IJ = np.linalg.inv(JM1)
        #print('Inverse Jacobian  Matrix = ', IJ)
        sg.popup('Inverse Jacobian Matrix = ',np.around(IJ,3))
        
    elif event == 'Transpose of J':
        # Transpose of Jacobian Matrix
        try:
            JM1 = np.concatenate((J1,J2,J3),1)
        except:
            JM1 = -1 #NAN
            sg.popup('Warning! The TOP button was not pressed!')
            sg.popup('Restart the GUI and click the TOP button to generate calculator!')
            break
            
        TJ = np.transpose(JM1)
        #print('Transpose of Jacobian Matrix = ', TJ)
        
        sg.popup('Transpose of Jacobian Matrix = ', TJ)
        
    elif event == 'Solve Inverse Kinematics':
        Inverse_Kinematics_window()
            
window.close()
