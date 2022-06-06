import quantumrandom as qt
import eel
eel.init('web')

@eel.expose    
def tarot12(data):
    
        
    data = data.split(" ")
    q = int(data[0])
    w = int(data[1])
    e = int(data[2])
    r = int(data[3])
    t = int(data[4])
    y = int(data[5])
    u = int(data[6])
    i = int(data[7])
    o = int(data[8])
    p = int(data[9])
    a = int(data[10])
    s = int(data[11])
    
    
    k = qt.get_data(data_type='uint16', array_length=2)

    binary = ""
    #generating a string of 31 binary numbers for entropy. 
    for integer in k:
        binary = binary + bin(integer)[2:]

    shuffle_number = s

    print("SHUFFLED NUMBER IS {}".format(shuffle_number))

    deck= [
        { "imgrev":"reverse/rev00.jpg","color":"Yellow","name" : "The Fool", "url" : "the_fool", "image" : "major/00.jpg", "desc" : "Immaturity, sincerity, the natural man, a free spirit. One who naturally knows his will and is worry free. A dreamer, careless and disinterested in practical matters. Travel." , "rdesc" : "Folly, failure, madness. Hindered travel." },
        {"imgrev":"reverse/rev01.jpg","color":"Yellow", "name" : "The Magician", "url" : "the_magician", "image" : "major/01.jpg" , "desc" : "Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where he is going and how to achieve its ends." , "rdesc" : "Indecision, weak will, ineptitude, dilettante. Deceitfulness, trickery." },
        {"imgrev":"reverse/rev02.jpg","color":"Blue", "name" : "The High Priestess", "url" : "the_high_priestess", "image" : "major/02.jpg" , "desc" : "Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition, possibly given by a woman. Psychic ability. The manifestation of the eternal feminine in a spiritual way." , "rdesc" : "Deceptive, secret, or sly manner. Lazyness, intolerance. Delays. False ideas, moodiness, doubt, superficiality." },
        {"imgrev":"reverse/rev03.jpg", "color":"Green","name" : "The Empress", "url" : "the_empress", "image" : "major/03.jpg" , "desc" : "Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development." , "rdesc" : "False appearance, vanity, disdain, frivolity. Sterility. Delays. Careless spending." },
        { "imgrev":"reverse/rev04.jpg","color":"Red","name" : "The Emperor", "url" : "the_emperor", "image" : "major/04.jpg" , "desc" : "Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person." , "rdesc" : "Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac." },
        { "imgrev":"reverse/rev05.jpg","color":"#ff5349","name" : "The Hierophant", "url" : "the_hierophant", "image" : "major/05.jpg" , "desc" : "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart. The card that represents you, in the form of your own, truest voice, your own inner-self. Dogma. Can be lawyers." , "rdesc" : "Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently." },
        { "imgrev":"reverse/rev06.jpg","color":"Orange","name" : "The Lovers", "url" : "the_lovers", "image" : "major/06.jpg" , "desc" : "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life." , "rdesc" : "Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation." },
        { "imgrev":"reverse/rev07.jpg","color":"#ffae42","name" : "The Chariot", "url" : "the_chariot", "image" : "major/07.jpg" , "desc" : "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel." , "rdesc" : "Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accidente." },
        { "imgrev":"reverse/rev08.jpg","color":"Yellow","name" : "Strength", "url" : "strength", "image" : "major/08.jpg" , "desc" : "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust." , "rdesc" : "Discord, ruin, stubbornness, abuse of power. Weakness." },
        { "imgrev":"reverse/rev09.jpg","color":"#9acd32","name" : "The Hermit", "url" : "the_hermit", "image" : "major/09.jpg" , "desc" : "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development." , "rdesc" : "Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies." },
        {"imgrev":"reverse/rev10.jpg", "color":"violet","name" : "The Wheel of Fortune", "url" : "the_wheel_of_fortune", "image" : "major/10.jpg" , "desc" : "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions." , "rdesc" : "Retarded progress. Delays, setbacks." },
        {"imgrev":"reverse/rev11.jpg","color":"green", "name" : "Justice", "url" : "justice", "image" : "major/11.jpg" , "desc" : "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed.. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation." , "rdesc" : "Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance." },
        { "imgrev":"reverse/rev12.jpg","color":"blue","name" : "The Hanged Man", "url" : "the_hanged_man", "image" : "major/12.jpg" , "desc" : "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation." , "rdesc" : "Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure." },
        { "imgrev":"reverse/rev13.jpg","color":"#0d98ba","name" : "Death", "url" : "death", "image" : "major/13.jpg" , "desc" : "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another." , "rdesc" : "Stagnation, death, petrification. Incurable ill person. Broken marriage." },
        { "imgrev":"reverse/rev14.jpg","color":"blue","name" : "Temperance", "url" : "temperance", "image" : "major/14.jpg" , "desc" : "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will." , "rdesc" : "Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck." },
        { "imgrev":"reverse/rev15.jpg","color":"indigo","name" : "The Devil", "url" : "the_devil", "image" : "major/15.jpg" , "desc" : "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out." , "rdesc" : "Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth." },
        { "imgrev":"reverse/rev16.jpg","color":"red","name" : "The Blasted Tower", "url" : "the_blasted_tower", "image" : "major/16.jpg" , "desc" : "Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. Finger of God. Bankruptcy. Sudden death." , "rdesc" : "Complete confusion. The gain of freedom at great cost. False accusations, oppression." },
        { "imgrev":"reverse/rev17.jpg","color":"violet","name" : "The Star", "url" : "the_star", "image" : "major/17.jpg" , "desc" : "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health." , "rdesc" : "Arrogance, pessimism, stubbornness. Illness. Error of judgment." },
        { "imgrev":"reverse/rev18.jpg","color":"#c71585","name" : "The Moon", "url" : "the_moon", "image" : "major/18.jpg" , "desc" : " You need to be aware of the situations that are causing fear and anxiety in your mind, whether it is now or in the future. It alerts you not to allow inner disturbances and self-deception to take the best of you. These deep memories and fears must be let go, and the negative energies must be released and turned into something constructive.  Intuition, threshold of an important change, arduous and obscure path, development of psychic powers." , "rdesc" : "Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer." },
        { "imgrev":"reverse/rev19.jpg","color":"orange","name" : "The Sun", "url" : "the_sun", "image" : "major/19.jpg" , "desc" : "Because of your own personal fulfillment, you provide others with inspiration and joy as well. People are drawn to you because they are capable of seeing the warm and beautiful energy which you bring into their lives. You are also in a position in which you are capable of sharing your qualities as well as achievements with other people. You radiate love and affection towards those you care about the most. /nGlory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others." , "rdesc" : "Anoyances, disguise. Arrogance. Broken engagement or lost job." },
        { "imgrev":"reverse/rev20.jpg","color":"red","name" : "Judgement", "url" : "judgement", "image" : "major/20.jpg" , "desc" : "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor./nTo see this card can also indicate that you are in a period of awakening, brought on by the act of self-reflection. You now have a clearer idea of what you need to change and how you need to be true yourself and your needs. This can mean making small changes to your daily life or making huge changes that not only affect you but the people close to you" , "rdesc" : "Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment." },
        { "imgrev":"reverse/rev21.jpg","color":"indigo","name" : "The World", "url" : "the_world", "image" : "major/21.jpg" , "desc" : "Success granted. Rewards. Travel, emigration, change of residence./nThe meaning of the World card is fulfillment, achievement, and completion. This shows that all the efforts that you have been putting in place are starting to pay off. It reflects that you have completed a major milestone in your life and you have built the resilience to withstand challenges. The World may indicate completion of a long-term project, study or any other major event in your life. It may also mean the birth of a child, marriage, graduation or any other thing that you have accomplished." , "rdesc" : "Hindrances, stagnation. Hard work to bring success./n" }
        
    ]
    print(len(deck))
    for i in range(0,len(deck)):
        j = i + shuffle_number
        if j > 21:
            j = j%22
 
        deck[i],deck[j] = deck[j],deck[i]
        
    shuff = deck
    q1 = shuff[q]
    q11 = binary[q]
    w1 = shuff[w]
    w11 = binary[w]
    e1 = shuff[e]
    e11 = binary[e]
    r1 = shuff[r]
    r11 = binary[r]
    t1 = shuff[t]
    t11 = binary[t]
    y1 = shuff[y]
    y11 = binary[y]
    u1 = shuff[u]
    u11 = binary[u]
    i1 = shuff[i]
    i11= binary[i]
    o1 = shuff[o]
    o11 = binary[o]
    p1 = shuff[p]
    p11 = binary[p]
    a1 = shuff[a]
    a11 = binary[a]
    s1 = shuff[s]
    s11 = binary[s]



    if q11 == '0':
        im0 = q1["imgrev"]
        
        
        
    if q11 == '1':
        im0 = q1["image"]
    if w11 == "0":
        im1 = w1["imgrev"]
    if w11 == "1":
        im1 = w1["image"]
    if e11 == "0":
        im2 = e1["imgrev"]
    if e11 == "1":
        im2 = e1["image"]
    if r11 == "0":
        im3 = r1["imgrev"]
    if r11 == "1":
        im3 = r1["image"]

    if t11 == "0":
        im4 = t1["imgrev"]
    if t11 == "1":
        im4 = t1["image"]

    if y11 == "0":
        im5 = y1["imgrev"]
    if y11 == "1":
        im5 = y1["image"]

    if u11 == "0":
        im6 = u1["imgrev"]
    if u11 == "1":
        im6 = u1["image"]

    if i11 == "0":
        im7 = i1["imgrev"]
    if i11 == "1":
        im7 = i1["image"]

    if o11 == "0":
        im8 = r1["imgrev"]
    if o11 == "1":
        im8 = r1["image"]

    if p11 == "0":
        im9 = p1["imgrev"]
    if p11 == "1":
        im9 = p1["image"]

    if a11 == "0":
        im10 = a1["imgrev"]
    if a11 == "1":
        im10 = a1["image"]

    if s11 == "0":
        im11 = s1["imgrev"]
    if s11 == "1":
        im11 = s1["image"]

    
    
    return im0,im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im10,im11

@eel.expose        
def tarot7(data):
    data = data.split(" ")
    q = int(data[0])
    w = int(data[1])
    e = int(data[2])
    r = int(data[3])
    t = int(data[4])
    y = int(data[5])
    u = int(data[6])

    
    
    k = qt.get_data(data_type='uint16', array_length=2)

    binary = ""
    #generating a string of 31 binary numbers for entropy. 
    for integer in k:
        binary = binary + bin(integer)[2:]
   
    shuffle_number = u

    print("SHUFFLED NUMBER IS {}".format(shuffle_number))

    deck= [
        { "imgrev":"reverse/rev00.jpg","color":"Yellow","name" : "The Fool", "url" : "the_fool", "image" : "major/00.jpg", "desc" : "Immaturity, sincerity, the natural man, a free spirit. One who naturally knows his will and is worry free. A dreamer, careless and disinterested in practical matters. Travel." , "rdesc" : "Folly, failure, madness. Hindered travel." },
        {"imgrev":"reverse/rev01.jpg","color":"Yellow", "name" : "The Magician", "url" : "the_magician", "image" : "major/01.jpg" , "desc" : "Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where he is going and how to achieve its ends." , "rdesc" : "Indecision, weak will, ineptitude, dilettante. Deceitfulness, trickery." },
        {"imgrev":"reverse/rev02.jpg","color":"Blue", "name" : "The High Priestess", "url" : "the_high_priestess", "image" : "major/02.jpg" , "desc" : "Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition, possibly given by a woman. Psychic ability. The manifestation of the eternal feminine in a spiritual way." , "rdesc" : "Deceptive, secret, or sly manner. Lazyness, intolerance. Delays. False ideas, moodiness, doubt, superficiality." },
        {"imgrev":"reverse/rev03.jpg", "color":"Green","name" : "The Empress", "url" : "the_empress", "image" : "major/03.jpg" , "desc" : "Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development." , "rdesc" : "False appearance, vanity, disdain, frivolity. Sterility. Delays. Careless spending." },
        { "imgrev":"reverse/rev04.jpg","color":"Red","name" : "The Emperor", "url" : "the_emperor", "image" : "major/04.jpg" , "desc" : "Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person." , "rdesc" : "Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac." },
        { "imgrev":"reverse/rev05.jpg","color":"#ff5349","name" : "The Hierophant", "url" : "the_hierophant", "image" : "major/05.jpg" , "desc" : "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart. The card that represents you, in the form of your own, truest voice, your own inner-self. Dogma. Can be lawyers." , "rdesc" : "Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently." },
        { "imgrev":"reverse/rev06.jpg","color":"Orange","name" : "The Lovers", "url" : "the_lovers", "image" : "major/06.jpg" , "desc" : "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life." , "rdesc" : "Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation." },
        { "imgrev":"reverse/rev07.jpg","color":"#ffae42","name" : "The Chariot", "url" : "the_chariot", "image" : "major/07.jpg" , "desc" : "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel." , "rdesc" : "Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accidente." },
        { "imgrev":"reverse/rev08.jpg","color":"Yellow","name" : "Strength", "url" : "strength", "image" : "major/08.jpg" , "desc" : "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust." , "rdesc" : "Discord, ruin, stubbornness, abuse of power. Weakness." },
        { "imgrev":"reverse/rev09.jpg","color":"#9acd32","name" : "The Hermit", "url" : "the_hermit", "image" : "major/09.jpg" , "desc" : "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development." , "rdesc" : "Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies." },
        {"imgrev":"reverse/rev10.jpg", "color":"violet","name" : "The Wheel of Fortune", "url" : "the_wheel_of_fortune", "image" : "major/10.jpg" , "desc" : "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions." , "rdesc" : "Retarded progress. Delays, setbacks." },
        {"imgrev":"reverse/rev11.jpg","color":"green", "name" : "Justice", "url" : "justice", "image" : "major/11.jpg" , "desc" : "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed.. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation." , "rdesc" : "Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance." },
        { "imgrev":"reverse/rev12.jpg","color":"blue","name" : "The Hanged Man", "url" : "the_hanged_man", "image" : "major/12.jpg" , "desc" : "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation." , "rdesc" : "Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure." },
        { "imgrev":"reverse/rev13.jpg","color":"#0d98ba","name" : "Death", "url" : "death", "image" : "major/13.jpg" , "desc" : "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another." , "rdesc" : "Stagnation, death, petrification. Incurable ill person. Broken marriage." },
        { "imgrev":"reverse/rev14.jpg","color":"blue","name" : "Temperance", "url" : "temperance", "image" : "major/14.jpg" , "desc" : "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will." , "rdesc" : "Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck." },
        { "imgrev":"reverse/rev15.jpg","color":"indigo","name" : "The Devil", "url" : "the_devil", "image" : "major/15.jpg" , "desc" : "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out." , "rdesc" : "Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth." },
        { "imgrev":"reverse/rev16.jpg","color":"red","name" : "The Blasted Tower", "url" : "the_blasted_tower", "image" : "major/16.jpg" , "desc" : "Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. Finger of God. Bankruptcy. Sudden death." , "rdesc" : "Complete confusion. The gain of freedom at great cost. False accusations, oppression." },
        { "imgrev":"reverse/rev17.jpg","color":"violet","name" : "The Star", "url" : "the_star", "image" : "major/17.jpg" , "desc" : "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health." , "rdesc" : "Arrogance, pessimism, stubbornness. Illness. Error of judgment." },
        { "imgrev":"reverse/rev18.jpg","color":"#c71585","name" : "The Moon", "url" : "the_moon", "image" : "major/18.jpg" , "desc" : " You need to be aware of the situations that are causing fear and anxiety in your mind, whether it is now or in the future. It alerts you not to allow inner disturbances and self-deception to take the best of you. These deep memories and fears must be let go, and the negative energies must be released and turned into something constructive.  Intuition, threshold of an important change, arduous and obscure path, development of psychic powers." , "rdesc" : "Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer." },
        { "imgrev":"reverse/rev19.jpg","color":"orange","name" : "The Sun", "url" : "the_sun", "image" : "major/19.jpg" , "desc" : "Because of your own personal fulfillment, you provide others with inspiration and joy as well. People are drawn to you because they are capable of seeing the warm and beautiful energy which you bring into their lives. You are also in a position in which you are capable of sharing your qualities as well as achievements with other people. You radiate love and affection towards those you care about the most. /nGlory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others." , "rdesc" : "Anoyances, disguise. Arrogance. Broken engagement or lost job." },
        { "imgrev":"reverse/rev20.jpg","color":"red","name" : "Judgement", "url" : "judgement", "image" : "major/20.jpg" , "desc" : "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor./nTo see this card can also indicate that you are in a period of awakening, brought on by the act of self-reflection. You now have a clearer idea of what you need to change and how you need to be true yourself and your needs. This can mean making small changes to your daily life or making huge changes that not only affect you but the people close to you" , "rdesc" : "Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment." },
        { "imgrev":"reverse/rev21.jpg","color":"indigo","name" : "The World", "url" : "the_world", "image" : "major/21.jpg" , "desc" : "Success granted. Rewards. Travel, emigration, change of residence./nThe meaning of the World card is fulfillment, achievement, and completion. This shows that all the efforts that you have been putting in place are starting to pay off. It reflects that you have completed a major milestone in your life and you have built the resilience to withstand challenges. The World may indicate completion of a long-term project, study or any other major event in your life. It may also mean the birth of a child, marriage, graduation or any other thing that you have accomplished." , "rdesc" : "Hindrances, stagnation. Hard work to bring success./n" }
        
    ]
    print(len(deck))
    for i in range(0,len(deck)):
        j = i + shuffle_number
        if j > 21:
            j = j%22
   
        deck[i],deck[j] = deck[j],deck[i]
        
    shuff = deck
    q1 = shuff[q]
    q11 = binary[q]
    w1 = shuff[w]
    w11 = binary[w]
    e1 = shuff[e]
    e11 = binary[e]
    r1 = shuff[r]
    r11 = binary[r]
    t1 = shuff[t]
    t11 = binary[t]
    y1 = shuff[y]
    y11 = binary[y]
    u1 = shuff[u]
    u11 = binary[u]




    if q11 == '0':
        im0 = q1["imgrev"]
        
        
        
    if q11 == '1':
        im0 = q1["image"]
    if w11 == "0":
        im1 = w1["imgrev"]
    if w11 == "1":
        im1 = w1["image"]
    if e11 == "0":
        im2 = e1["imgrev"]
    if e11 == "1":
        im2 = e1["image"]
    if r11 == "0":
        im3 = r1["imgrev"]
    if r11 == "1":
        im3 = r1["image"]

    if t11 == "0":
        im4 = t1["imgrev"]
    if t11 == "1":
        im4 = t1["image"]

    if y11 == "0":
        im5 = y1["imgrev"]
    if y11 == "1":
        im5 = y1["image"]

    if u11 == "0":
        im6 = u1["imgrev"]
    if u11 == "1":
        im6 = u1["image"]



    
    return im0,im1,im2,im3,im4,im5,im6

@eel.expose
def tarot4(data):
    
        
    data = data.split(" ")
    q = int(data[0])
    w = int(data[1])
    e = int(data[2])
    r = int(data[3])

    
    k = qt.get_data(data_type='uint16', array_length=2)

    binary = ""
    #generating a string of 31 binary numbers for entropy. 
    for integer in k:
        binary = binary + bin(integer)[2:]
    print(binary)
    print("\n")
    print(len(binary))
    shuffle_number = r

    print("SHUFFLED NUMBER IS {}".format(shuffle_number))

    deck= [
        { "imgrev":"reverse/rev00.jpg","color":"Yellow","name" : "The Fool", "url" : "the_fool", "image" : "major/00.jpg", "desc" : "Immaturity, sincerity, the natural man, a free spirit. One who naturally knows his will and is worry free. A dreamer, careless and disinterested in practical matters. Travel." , "rdesc" : "Folly, failure, madness. Hindered travel." },
        {"imgrev":"reverse/rev01.jpg","color":"Yellow", "name" : "The Magician", "url" : "the_magician", "image" : "major/01.jpg" , "desc" : "Will, creativeness, adroitness, mastery, elasticity, autonomy, eloquence, craft, cunning. May imply a new beginning. The Magus is an autonomous person that knows where he is going and how to achieve its ends." , "rdesc" : "Indecision, weak will, ineptitude, dilettante. Deceitfulness, trickery." },
        {"imgrev":"reverse/rev02.jpg","color":"Blue", "name" : "The High Priestess", "url" : "the_high_priestess", "image" : "major/02.jpg" , "desc" : "Hidden influence. Silence, patience, equilibrium. Slow but firm. Pondered decision. Advice, tuition, possibly given by a woman. Psychic ability. The manifestation of the eternal feminine in a spiritual way." , "rdesc" : "Deceptive, secret, or sly manner. Lazyness, intolerance. Delays. False ideas, moodiness, doubt, superficiality." },
        {"imgrev":"reverse/rev03.jpg", "color":"Green","name" : "The Empress", "url" : "the_empress", "image" : "major/03.jpg" , "desc" : "Understanding, charm, kindness, beauty, pleasure, success, safety, trust. Nurturing, positive development." , "rdesc" : "False appearance, vanity, disdain, frivolity. Sterility. Delays. Careless spending." },
        { "imgrev":"reverse/rev04.jpg","color":"Red","name" : "The Emperor", "url" : "the_emperor", "image" : "major/04.jpg" , "desc" : "Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person." , "rdesc" : "Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac." },
        { "imgrev":"reverse/rev05.jpg","color":"#ff5349","name" : "The Hierophant", "url" : "the_hierophant", "image" : "major/05.jpg" , "desc" : "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart. The card that represents you, in the form of your own, truest voice, your own inner-self. Dogma. Can be lawyers." , "rdesc" : "Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently." },
        { "imgrev":"reverse/rev06.jpg","color":"Orange","name" : "The Lovers", "url" : "the_lovers", "image" : "major/06.jpg" , "desc" : "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life." , "rdesc" : "Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation." },
        { "imgrev":"reverse/rev07.jpg","color":"#ffae42","name" : "The Chariot", "url" : "the_chariot", "image" : "major/07.jpg" , "desc" : "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel." , "rdesc" : "Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accidente." },
        { "imgrev":"reverse/rev08.jpg","color":"Yellow","name" : "Strength", "url" : "strength", "image" : "major/08.jpg" , "desc" : "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust." , "rdesc" : "Discord, ruin, stubbornness, abuse of power. Weakness." },
        { "imgrev":"reverse/rev09.jpg","color":"#9acd32","name" : "The Hermit", "url" : "the_hermit", "image" : "major/09.jpg" , "desc" : "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development." , "rdesc" : "Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies." },
        {"imgrev":"reverse/rev10.jpg", "color":"violet","name" : "The Wheel of Fortune", "url" : "the_wheel_of_fortune", "image" : "major/10.jpg" , "desc" : "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions." , "rdesc" : "Retarded progress. Delays, setbacks." },
        {"imgrev":"reverse/rev11.jpg","color":"green", "name" : "Justice", "url" : "justice", "image" : "major/11.jpg" , "desc" : "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed.. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation." , "rdesc" : "Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance." },
        { "imgrev":"reverse/rev12.jpg","color":"blue","name" : "The Hanged Man", "url" : "the_hanged_man", "image" : "major/12.jpg" , "desc" : "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation." , "rdesc" : "Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure." },
        { "imgrev":"reverse/rev13.jpg","color":"#0d98ba","name" : "Death", "url" : "death", "image" : "major/13.jpg" , "desc" : "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another." , "rdesc" : "Stagnation, death, petrification. Incurable ill person. Broken marriage." },
        { "imgrev":"reverse/rev14.jpg","color":"blue","name" : "Temperance", "url" : "temperance", "image" : "major/14.jpg" , "desc" : "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will." , "rdesc" : "Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck." },
        { "imgrev":"reverse/rev15.jpg","color":"indigo","name" : "The Devil", "url" : "the_devil", "image" : "major/15.jpg" , "desc" : "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out." , "rdesc" : "Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth." },
        { "imgrev":"reverse/rev16.jpg","color":"red","name" : "The Blasted Tower", "url" : "the_blasted_tower", "image" : "major/16.jpg" , "desc" : "Sudden changes without choice, collapse, escape from prison or bondages, accident. Plans will fall, intentions will break down. Finger of God. Bankruptcy. Sudden death." , "rdesc" : "Complete confusion. The gain of freedom at great cost. False accusations, oppression." },
        { "imgrev":"reverse/rev17.jpg","color":"violet","name" : "The Star", "url" : "the_star", "image" : "major/17.jpg" , "desc" : "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health." , "rdesc" : "Arrogance, pessimism, stubbornness. Illness. Error of judgment." },
        { "imgrev":"reverse/rev18.jpg","color":"#c71585","name" : "The Moon", "url" : "the_moon", "image" : "major/18.jpg" , "desc" : " You need to be aware of the situations that are causing fear and anxiety in your mind, whether it is now or in the future. It alerts you not to allow inner disturbances and self-deception to take the best of you. These deep memories and fears must be let go, and the negative energies must be released and turned into something constructive.  Intuition, threshold of an important change, arduous and obscure path, development of psychic powers." , "rdesc" : "Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer." },
        { "imgrev":"reverse/rev19.jpg","color":"orange","name" : "The Sun", "url" : "the_sun", "image" : "major/19.jpg" , "desc" : "Because of your own personal fulfillment, you provide others with inspiration and joy as well. People are drawn to you because they are capable of seeing the warm and beautiful energy which you bring into their lives. You are also in a position in which you are capable of sharing your qualities as well as achievements with other people. You radiate love and affection towards those you care about the most. /nGlory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others." , "rdesc" : "Anoyances, disguise. Arrogance. Broken engagement or lost job." },
        { "imgrev":"reverse/rev20.jpg","color":"red","name" : "Judgement", "url" : "judgement", "image" : "major/20.jpg" , "desc" : "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor./nTo see this card can also indicate that you are in a period of awakening, brought on by the act of self-reflection. You now have a clearer idea of what you need to change and how you need to be true yourself and your needs. This can mean making small changes to your daily life or making huge changes that not only affect you but the people close to you" , "rdesc" : "Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment." },
        { "imgrev":"reverse/rev21.jpg","color":"indigo","name" : "The World", "url" : "the_world", "image" : "major/21.jpg" , "desc" : "Success granted. Rewards. Travel, emigration, change of residence./nThe meaning of the World card is fulfillment, achievement, and completion. This shows that all the efforts that you have been putting in place are starting to pay off. It reflects that you have completed a major milestone in your life and you have built the resilience to withstand challenges. The World may indicate completion of a long-term project, study or any other major event in your life. It may also mean the birth of a child, marriage, graduation or any other thing that you have accomplished." , "rdesc" : "Hindrances, stagnation. Hard work to bring success./n" }
        
    ]
    print(len(deck))
    for i in range(0,len(deck)):
        j = i + shuffle_number
        if j > 21:
            j = j%22
        print(i)
        print("Now J")
        print(j)
        deck[i],deck[j] = deck[j],deck[i]
        
    shuff = deck
    q1 = shuff[q]
    q11 = binary[q]
    w1 = shuff[w]
    w11 = binary[w]
    e1 = shuff[e]
    e11 = binary[e]
    r1 = shuff[r]
    r11 = binary[r]



    if q11 == '0':
        im0 = q1["imgrev"]   
    if q11 == '1':
        im0 = q1["image"]
    if w11 == "0":
        im1 = w1["imgrev"]
    if w11 == "1":
        im1 = w1["image"]
    if e11 == "0":
        im2 = e1["imgrev"]
    if e11 == "1":
        im2 = e1["image"]
    if r11 == "0":
        im3 = r1["imgrev"]
    if r11 == "1":
        im3 = r1["image"]



    
    
    return im0,im1,im2,im3
        

eel.start('main_page.html', size=(786, 786))

        

                
