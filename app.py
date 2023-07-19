import streamlit as st
import pandas as pd
questions = [
    "Je me sens émotionnellement épuis(e) par mon travail:",
    "Je me sens à bout à la fin de ma journée de travail:",
    "Je me sens fatigué(e) quand je me lève le matin et que j'ai à affronter une nouvelle journée de travail:",
    "Je peux comprendre facilement ce que mes clients et autres interlocuteurs ressentent:",
    "Je sens que je m'occupe de certains clients de façon impersonnelle, comme s'ils étaient des objets:",
    "Travailler avec des gens tout au long de la journée me demande beaucoup d'effort:",
    "Je m'occupe très efficacement des problèmes de mes clients et autres interlocuteurs:",
    "Je sens que je craque à cause de mon travail:",
    "J'ai l'impression, à travers mon travail, d'avoir une influence positive sur les gens:",
    "Je suis devenu(e) plus insensible aux gens depuis que j'ai ce travail:",
    "Je crains que ce travail ne m'endurcisse émotionnellement:",
    "Je me sens plein(e) d'énergie:",
    "Je me sens frustré(e) par mon travail:",
    "Je sens que je travaille 'trop dur' dans mon travail:",
    "Je ne me soucie pas vraiment de ce qui arrive à certains de mes clients ou autres interlocuteurs:",
    "Travailler en contact direct avec les gens me stresse trop:",
    "J'arrive facilement à créer une atmosphère détendue avec mes clients et autres interlocuterusr:",
    "Je me sens ragaillardi(e) lorsque dans mon travail j'ai été proche de clients et autres interlocuterus:",
    "J'ai accompli beaucoup de choses qui en valent la peine dans ce travail:",
    "Je me sens au bout du rouleau:",
    "Dans mon travail, e traite les problmes émotionnels très calmement:",
    "J'ai l'impression que mes clients et autres interlocuteurs me rendent responsable de certains de leurs problèmes:",
    # Add the rest of your questions here
]

radio_options = {
    "Jamais": 0,
    "Plusieurs fois par an": 1,
    "Au moins une fois par mois": 2,
    "Plusieurs fois par mois": 3,
    "Au moins 1 fois par semaine": 4,
    "Plusieurs fois par semaine": 5,
    "Chaque jour": 6
}


def get_color(val, steps):
    if val <= steps[0]:
        return 'background-color: green'
    elif val <= steps[1]:
        return 'background-color: yellow'
    else:
        return 'background-color: red'


def main():
    st.title("Score Calculator")

    responses = {}

    for i, question in enumerate(questions):
        st.subheader(f"Question {i + 1}:")
        selected_option = st.radio(question, list(radio_options.keys()), 0)

        # Update the score based on the selected option
        responses[i] = radio_options[selected_option]
    
    scores = [
        {'name':'score_sep', 'indices': [0,1,2,5,7,12,13,15,19], 'steps':[17,29]},
        {'name':'score_sd', 'indices': [4,9,10,14,21], 'steps':[5, 11]},
        {'name':'score_sap', 'indices': [3,6,8,11,16,17,18,20], 'steps':[33,39]}
    ]

    if st.button('Calculer les scores'):
        data = []
        st.write(f'{responses}')
        for idx, el in enumerate(scores):
            # st.write(f'{[responses[i] for i in el["indices"]]}')
            res = sum(responses[i] for i in el['indices'])
            scores[idx]['Score'] = res
            scores[idx]['Color'] = get_color(res, scores[idx]['steps'])
            # print(el['indices'])
            # st.write(f"{el['name']}: {res}")
            # data.append({'Score': el['name'] , 'Valeur': res, 'Steps': el['steps']})
        print(scores)

        
        df = pd.DataFrame(scores).set_index('Name')
        # st.dataframe(df)
        styled_df = df.style.apply(lambda x:x['Color'])
        st.dataframe(styled_df['Score'])
            
    # st.subheader("Your Total Score:")
    # st.write(score)


if __name__ == "__main__":
    main()
