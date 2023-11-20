import random
import cassiopeia as cass
import PySimpleGUI as sg

cass.set_riot_api_key("")  # here you need to get a DEVELOPMENT API KEY from "https://developer.riotgames.com/" and insert it. itll expire in 24hours unless you register the application for a more permanent key

layout = [[sg.Text('Enter User Name: '), sg.InputText()],
          [sg.Text('Enter region: '), sg.InputText()],
          [sg.Button('Get Summoner Information'), sg.Button('Exit')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT2-')],
          [sg.Text(size=(40,1), key='-OUTPUT3-')],
          [sg.Text(size=(40,1), key='-OUTPUT4-')]]

window = sg.Window('Summoner Information', layout, size=(600, 250))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    SummonerName = values[0]
    RegionCode = values[1]

    # Get summoner information
    summoner = cass.get_summoner(name=SummonerName, region=RegionCode)

    # Get ranked information
    ranked_info = summoner.league_entries
    if len(ranked_info) > 0:
        rank = ranked_info[0]
        rank_str = f"Rank: {rank.tier} {rank.division} ({rank.league_points} LP)"
    else:
        rank_str = "Unranked"

    # Print summoner information
    window['-OUTPUT-'].update(f"Summoner Name: {summoner.name}")
    window['-OUTPUT2-'].update(f"Region: {summoner.region}")
    window['-OUTPUT3-'].update(f"Level: {summoner.level}")
    window['-OUTPUT4-'].update(f"{rank_str}")

window.close()
