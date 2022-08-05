import PySimpleGUI as sg
import MinizincAPI as mapi

####
### Funcion principal
def main():

    posY = ''
    posX = ''
    tiempo = 0
    n=0
    ciudades=0
    ciudadesCoordenadas=[]
    sg.theme('DarkPurple1')

    header = [
        [sg.Text('Asigna la ubicación de tu nueva Universidad!', 
        justification='center',
        font=('Helvetica', 15)
        )]
    ]

    body = [
        [sg.Text("Debes de ingresar las coordenadas de las ciudades, el primer campo es para \nla  abscisa y la segunda para la ordenada. Después presiona guardar \ncoordenada, puedes ingresar cuantas quieras!", 
        justification='left',
        font=('Helvetica', 10),
        )]
    ]

    column1 = [
        [sg.Text('Ingrese la dimensión del area',
        justification='center')],
        [sg.Text('Dimensión'), sg.Input(key='-N-',size=(5,1))],    
        [sg.Text('Ingrese una nueva coordenada de \nuna ciudad',
            justification='center')],
        [sg.Text('Coordenada en X'), sg.Input(key='X',size=(5,1))],
        [sg.Text('Coordenada en Y'), sg.Input(key='Y',size=(5,1))],
        [sg.Button("Crear",key='-ADD Ciudad-')]
        ]
        
    column2 = [
        [sg.T('Ciudades')],
        [sg.Button("Borrar todas!",key='-Delete-')]
    ]

    bottom = [
        [sg.Button("Resolver!",key='-Solving-')],
        [sg.Text('Las coordenadas de la ciudad deben ser:', justification='center')],
        [sg.Text('X: ' + str(posX), key= '-resx-' )], 
        [sg.Text('Y: ' + str(posY), key= '-resy-')], 
        [sg.Text('Tiempo: ' + str(round(tiempo,4)) + ' segundos', key= '-rest-')], 
    ]

    layout = [
        [
            [sg.Col(header, size = (None,None))],
            [sg.Col(body, size = (None,None))],
            [sg.Col(column1,size = (250,300)),sg.Col(column2, size = (250,300), scrollable=True, key='-COL-')],
            # [sg.Col(bottom, size = (None, 80))]
            [bottom]
        ]
    ]

    window = sg.Window('Proyecto Complejidad y Optimización', layout, size=(600, 600), grab_anywhere=False, element_justification='c')

    while True:
        event, values = window.read()
        #print(values)
        if event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            window.LoadFromDisk(filename)
            # load(form)
        elif event in ('Exit', None):
            break
        elif event == '-ADD Ciudad-':
            if  values['X'].isnumeric()  and values['Y'].isnumeric():
                window.extend_layout(window['-COL-'], [[sg.T('Ciudad X={}, Y={}'.format(values['X'], values['Y']),key=ciudades)]])
                window.visibility_changed()
                window['-COL-'].contents_changed()
                ciudadesCoordenadas.append([int(values['X']), int(values['Y'])])
                ciudades += 1
                if values['-N-'].isnumeric():
                    n = values['-N-']
        elif event == '-Delete-':
            ciudadesCoordenadas=[]
            for i in range(ciudades):
                window[i].update(visible=False)
                window[i].Widget.master.pack_forget() 
            window.visibility_changed()
            window['-COL-'].contents_changed()
            ciudades += 0
        elif event == '-Solving-':
            print(int(n),len(ciudadesCoordenadas),ciudadesCoordenadas)
            if len(ciudadesCoordenadas) > 0:
                posX, posY, tiempo = mapi.linkZinc(int(n), len(ciudadesCoordenadas), ciudadesCoordenadas)
                print(posX,posY, tiempo)
                window['-resx-'].update('X: ' + str(posX))
                window['-resy-'].update('Y: ' + str(posY))
                window['-rest-'].update('Tiempo: ' + str(round(tiempo,4)) + ' segundos')
    window.close()


if __name__ == '__main__':
    main()
    # import PySimpleGUI as sg

    # sg.theme_previewer()
