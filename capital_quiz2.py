import random

questions = [
    ("What is the capital of Brazil?", "Brasilia"),
    ("What is the capital of Jamaica?", "Kingston"),
    ("What is the capital of Poland?", "Warsaw"),
    ("What is the capital of Nepal?", "Kathmandu"),
    ("What is the capital of Malaysia?", "Kuala Lumpur"),
    ("What is the capital of Canada?", "Ottawa"),
    ("What is the capital of Argentina?", "Buenos Aires"),
    ("What is the capital of Australia?", "Canberra"),
    ("What is the capital of Chile?", "Santiago"),
    ("What is the capital of Egypt?", "Cairo"),
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the capital of Spain?", "Madrid"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the capital of Russia?", "Moscow"),
    ("What is the capital of China?", "Beijing"),
    ("What is the capital of Japan?", "Tokyo"),
    ("What is the capital of South Korea?", "Seoul"),
    ("What is the capital of Mexico?", "Mexico City"),
    ("What is the capital of India?", "New Delhi"),
    ("What is the capital of Afghanistan?", "Kabul"),
    ("What is the capital of Albania?", "Tirana"),
    ("What is the capital of Algeria?", "Algiers"),
    ("What is the capital of Andorra?", "Andorra la Vella"),
    ("What is the capital of Angola?", "Luanda"),
    ("What is the capital of Antigua and Barbuda?", "Saint John's"),
    ("What is the capital of Armenia?", "Yerevan"),
    ("What is the capital of Austria?", "Vienna"),
    ("What is the capital of Azerbaijan?", "Baku"),
    ("What is the capital of Bahamas?", "Nassau"),
    ("What is the capital of Bahrain?", "Manama"),
    ("What is the capital of Bangladesh?", "Dhaka"),
    ("What is the capital of Barbados?", "Bridgetown"),
    ("What is the capital of Belarus?", "Minsk"),
    ("What is the capital of Belgium?", "Brussels"),
    ("What is the capital of Belize?", "Belmopan"),
    ("What is the capital of Benin?", "Porto-Novo"),
    ("What is the capital of Bhutan?", "Thimphu"),
    ("What is the capital of Bolivia?", "Sucre"),
    ("What is the capital of Bosnia and Herzegovina?", "Sarajevo"),
    ("What is the capital of Botswana?", "Gaborone"),
    ("What is the capital of Brunei?", "Bandar Seri Begawan"),
    ("What is the capital of Bulgaria?", "Sofia"),
    ("What is the capital of Burkina Faso?", "Ouagadougou"),
    ("What is the capital of Burundi?", "Gitega"),
    ("What is the capital of Cambodia?", "Phnom Penh"),
    ("What is the capital of Cameroon?", "Yaounde"),
    ("What is the capital of Cape Verde?", "Praia"),
    ("What is the capital of the Central African Republic?", "Bangui"),
    ("What is the capital of Chad?", "N'Djamena"),
    ("What is the capital of Colombia?", "Bogota"),
    ("What is the capital of Costa Rica?", "San Jose"),
    ("What is the capital of Croatia?", "Zagreb"),
    ("What is the capital of Cuba?", "Havana"),
    ("What is the capital of Cyprus?", "Nicosia"),
    ("What is the capital of Czech Republic?", "Prague"),
    ("What is the capital of Denmark?", "Copenhagen"),
    ("What is the capital of Djibouti?", "Djibouti"),
    ("What is the capital of Dominica?", "Roseau"),
    ("What is the capital of the Dominican Republic?", "Santo Domingo"),
    ("What is the capital of East Timor?", "Dili"),
    ("What is the capital of Ecuador?", "Quito"),
    ("What is the capital of El Salvador?", "San Salvador"),
    ("What is the capital of Equatorial Guinea?", "Malabo"),
    ("What is the capital of Eritrea?", "Asmara"),
    ("What is the capital of Estonia?", "Tallinn"),
    ("What is the capital of Eswatini?", "Mbabane"),
    ("What is the capital of Ethiopia?", "Addis Ababa"),
    ("What is the capital of Fiji?", "Suva"),
    ("What is the capital of Finland?", "Helsinki"),
    ("What is the capital of Gabon?", "Libreville"),
    ("What is the capital of Gambia?", "Banjul"),
    ("What is the capital of Georgia?", "Tbilisi"),
    ("What is the capital of Ghana?", "Accra"),
    ("What is the capital of Greece?", "Athens"),
    ("What is the capital of Grenada?", "Saint George's"),
    ("What is the capital of Guatemala?", "Guatemala City"),
    ("What is the capital of Guinea?", "Conakry"),
    ("What is the capital of Guinea-Bissau?", "Bissau"),
    ("What is the capital of Guyana?", "Georgetown"),
    ("What is the capital of Haiti?", "Port-au-Prince"),
    ("What is the capital of Honduras?", "Tegucigalpa"),
    ("What is the capital of Hungary?", "Budapest"),
    ("What is the capital of Iceland?", "Reykjavik"),
    ("What is the capital of Indonesia?", "Jakarta"),
    ("What is the capital of Iran?", "Tehran"),
    ("What is the capital of Iraq?", "Baghdad"),
    ("What is the capital of Ireland?", "Dublin"),
    ("What is the capital of Israel?", "Jerusalem"),
    ("What is the capital of Ivory Coast?", "Yamoussoukro"),
    ("What is the capital of Jordan?", "Amman"),
    ("What is the capital of Kazakhstan?", "Astana"),
    ("What is the capital of Kenya?", "Nairobi"),
    ("What is the capital of Kuwait?", "Kuwait City"),
    ("What is the capital of Kyrgyzstan?", "Bishkek"),
    ("What is the capital of Laos?", "Vientiane"),
    ("What is the capital of Latvia?", "Riga"),
    ("What is the capital of Lebanon?", "Beirut"),
    ("What is the capital of Lesotho?", "Maseru"),
    ("What is the capital of Liberia?", "Monrovia"),
    ("What is the capital of Libya?", "Tripoli"),
    ("What is the capital of Liechtenstein?", "Vaduz"),
    ("What is the capital of Lithuania?", "Vilnius"),
    ("What is the capital of Luxembourg?", "Luxembourg"),
    ("What is the capital of Madagascar?", "Antananarivo"),
    ("What is the capital of Malawi?", "Lilongwe"),
    ("What is the capital of Maldives?", "Male"),
    ("What is the capital of Mali?", "Bamako"),
    ("What is the capital of Malta?", "Valletta"),
    ("What is the capital of Mauritania?", "Nouakchott"),
    ("What is the capital of Mauritius?", "Port Louis"),
    ("What is the capital of Micronesia?", "Palikir"),
    ("What is the capital of Moldova?", "Chisinau"),
    ("What is the capital of Monaco?", "Monaco"),
    ("What is the capital of Mongolia?", "Ulaanbaatar"),
    ("What is the capital of Montenegro?", "Podgorica"),
    ("What is the capital of Morocco?", "Rabat"),
    ("What is the capital of Mozambique?", "Maputo"),
    ("What is the capital of Myanmar?", "Naypyidaw"),
    ("What is the capital of Namibia?", "Windhoek"),
    ("What is the capital of Nauru?", "Yaren"),
    ("What is the capital of New Zealand?", "Wellington"),
    ("What is the capital of Nicaragua?", "Managua"),
    ("What is the capital of Niger?", "Niamey"),
    ("What is the capital of Nigeria?", "Abuja"),
    ("What is the capital of North Macedonia?", "Skopje"),
    ("What is the capital of Norway?", "Oslo"),
    ("What is the capital of Oman?", "Muscat"),
    ("What is the capital of Pakistan?", "Islamabad"),
    ("What is the capital of Panama?", "Panama City"),
    ("What is the capital of Papua New Guinea?", "Port Moresby"),
    ("What is the capital of Paraguay?", "Asuncion"),
    ("What is the capital of Peru?", "Lima"),
    ("What is the capital of Philippines?", "Manila"),
    ("What is the capital of Portugal?", "Lisbon"),
    ("What is the capital of Qatar?", "Doha"),
    ("What is the capital of Romania?", "Bucharest"),
    ("What is the capital of Rwanda?", "Kigali"),
    ("What is the capital of Samoa?", "Apia"),
    ("What is the capital of San Marino?", "San Marino"),
    ("What is the capital of Saudi Arabia?", "Riyadh"),
    ("What is the capital of Senegal?", "Dakar"),
    ("What is the capital of Serbia?", "Belgrade"),
    ("What is the capital of Seychelles?", "Victoria"),
    ("What is the capital of Sierra Leone?", "Freetown"),
    ("What is the capital of Singapore?", "Singapore"),
    ("What is the capital of Slovakia?", "Bratislava"),
    ("What is the capital of Slovenia?", "Ljubljana"),
    ("What is the capital of Solomon Islands?", "Honiara"),
    ("What is the capital of Somalia?", "Mogadishu"),
    ("What is the capital of South Africa?", "Pretoria"),
    ("What is the capital of South Sudan?", "Juba"),
    ("What is the capital of Sri Lanka?", "Sri Jayawardenepura Kotte"),
    ("What is the capital of Sudan?", "Khartoum"),
    ("What is the capital of Suriname?", "Paramaribo"),
    ("What is the capital of Sweden?", "Stockholm"),
    ("What is the capital of Switzerland?", "Bern"),
    ("What is the capital of Syria?", "Damascus"),
    ("What is the capital of Taiwan?", "Taipei"),
    ("What is the capital of Tajikistan?", "Dushanbe"),
    ("What is the capital of Tanzania?", "Dodoma"),
    ("What is the capital of Thailand?", "Bangkok"),
    ("What is the capital of Togo?", "Lome"),
    ("What is the capital of Tonga?", "Nuku'alofa"),
    ("What is the capital of Trinidad and Tobago?", "Port of Spain"),
    ("What is the capital of Tunisia?", "Tunis"),
    ("What is the capital of Turkey?", "Ankara"),
    ("What is the capital of Turkmenistan?", "Ashgabat"),
    ("What is the capital of Tuvalu?", "Funafuti"),
    ("What is the capital of Uganda?", "Kampala"),
    ("What is the capital of Ukraine?", "Kyiv"),
    ("What is the capital of United Arab Emirates?", "Abu Dhabi"),
    ("What is the capital of United Kingdom?", "London"),
    ("What is the capital of United States?", "Washington, D.C."),
    ("What is the capital of Uruguay?", "Montevideo"),
    ("What is the capital of Uzbekistan?", "Tashkent"),
    ("What is the capital of Vanuatu?", "Port Vila"),
    ("What is the capital of Vatican City?", "Vatican City"),
    ("What is the capital of Venezuela?", "Caracas"),
    ("What is the capital of Vietnam?", "Hanoi"),
    ("What is the capital of Yemen?", "Sana'a"),
    ("What is the capital of Zambia?", "Lusaka"),
    ("What is the capital of Zimbabwe?", "Harare")
]

# Função para verificar respostas
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer!")
            score += 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Wrong answer. Try again: ")
            attempt += 1

    if attempt == 3:
        print(f"The correct answer is {answer}.")

# Quadro de melhores pontuações
high_scores = []

# Função para jogar o jogo
def play_game():
    global score
    score = 0

    # Pegando o nome do jogador
    player_name = input("Enter your name: ")

    # Randomizando perguntas
    random.shuffle(questions)
    selected_questions = questions[:10]  # Seleciona 10 perguntas aleatoriamente

    for question, answer in selected_questions:
        guess = input(question + " ")
        check_guess(guess, answer)

    print(f"\n{player_name}, your final score is: {score}")

    # Adicionando ao quadro de melhores pontuações
    high_scores.append((player_name, score))
    high_scores.sort(key=lambda x: x[1], reverse=True)  # Ordena por pontuação

    # Exibindo o quadro de melhores pontuações
    print("\nHigh Scores:")
    for name, points in high_scores:
        print(f"{name}: {points}")

# Função principal
def main():
    print("Welcome to 'Guess the Capital'!")
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

# Iniciar o jogo
if __name__ == "__main__":
    main()
