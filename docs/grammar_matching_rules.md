# Hanabira Grammar Matching Rules

This document lists every grammar point in the local database along with the exact deterministic rules (String Markers and Token Formation Patterns) the engine automatically derived to match them.

## N5

### A が いちばん～ (A ga ichiban～)
**Original Formation String:** `Noun + が + いちばん + Adjective/Verb`
- **String Markers:** `がいちばん`, `いちばん`
- **Token Formation Patterns:**
  - [noun] + `が` + `いちばん` + [adjective] + [verb]

### A は B より～ (A wa B yori～)
**Original Formation String:** `A は B より + Adjective`
- **String Markers:** `より`
- **Token Formation Patterns:**
  - `は` + `より` + [adjective]

### A より B のほうが～ (A yori B no hou ga ～)
**Original Formation String:** `A + より + B + のほうが + Adjective`
- **String Markers:** `より`, `のほうが`
- **Token Formation Patterns:**
  - `より` + `のほうが` + [adjective]

### A。 では、～B。 (A. Dewa, ~B)
**Original Formation String:** `Noun A + では、 + Subject + Predicate B`
- **String Markers:** `では`
- **Token Formation Patterns:**
  - [noun] + `では`

### A。けれども、～B。(A. Keredomo,~ B.)
**Original Formation String:** `Statement A + けれども、+ Statement B`
- **String Markers:** `けれども`
- **Token Formation Patterns:** *None successfully parsed*

### A。しかし、～B。 (A. Shikashi, ~B.)
**Original Formation String:** `Sentence A + しかし + Sentence B.`
- **String Markers:** `しかし`
- **Token Formation Patterns:** *None successfully parsed*

### A。じゃ、～B。(A. Ja, ~B.)
**Original Formation String:** `A: Sentence, B: Sentence (A and B can be any sentence type)`
- **String Markers:** `じゃ`
- **Token Formation Patterns:** *None successfully parsed*

### A。それじゃ、～B。(A. Soreja,~B.)
**Original Formation String:** `Sentence A + 。それじゃ、 + Sentence B`
- **String Markers:** `それじゃ`
- **Token Formation Patterns:** *None successfully parsed*

### A。それでは、～B。(A. Soredewa,~B.)
**Original Formation String:** `A (Statement) + 。それでは、 + B (Follow-up action or statement)`
- **String Markers:** `それでは`
- **Token Formation Patterns:** *None successfully parsed*

### A。でも、～B。(A. Demo, ~B)
**Original Formation String:** `Clause A + でも + Clause B`
- **String Markers:** `でも`
- **Token Formation Patterns:** *None successfully parsed*

### Aと Bと どちら～ (A to B to dochira~)
**Original Formation String:** `Aと Bと どちら + Verb/Adjective/Noun`
- **String Markers:** `とどちら`
- **Token Formation Patterns:**
  - `と` + `と` + `どちら` + [verb] + [adjective] + [noun]

### AとBと どっち〜 (A to B to docchi〜)
**Original Formation String:** `AとBと どっち + Verb, AかBか どっち + Verb`
- **String Markers:** `とどっち`, `かどっち`
- **Token Formation Patterns:**
  - `と` + `と` + `どっち` + [verb] + `か` + `か` + `どっち` + [verb]

### Noun から Noun まで (Noun kara Noun made)
**Original Formation String:** `Noun1 + から + Noun2 + まで`
- **String Markers:** `から`, `まで`
- **Token Formation Patterns:**
  - [noun] + `から` + [noun] + `まで`

### Noun が できます (Noun ga dekimasu)
**Original Formation String:** `Noun + が + できます`
- **String Markers:** `ができます`, `できます`
- **Token Formation Patterns:**
  - [noun] + `が` + `できます`

### Noun がほしいです (〜ga hoshii desu)
**Original Formation String:** `Noun + が + ほしいです`
- **String Markers:** `がほしいです`, `ほしいです`
- **Token Formation Patterns:**
  - [noun] + `が` + `ほしいです`

### Noun くらい～ (Noun kurai～)
**Original Formation String:** `Noun + くらい`
- **String Markers:** `くらい`
- **Token Formation Patterns:**
  - [noun] + `くらい`

### Noun ぐらい～ (Noun gurai～)
**Original Formation String:** `Noun + ぐらい`
- **String Markers:** `ぐらい`
- **Token Formation Patterns:**
  - [noun] + `ぐらい`

### Noun ごろ～ (Noun + goro～)
**Original Formation String:** `Noun + ごろ`
- **String Markers:** `ごろ`
- **Token Formation Patterns:**
  - [noun] + `ごろ`

### Noun だけ〜 (〜dake)
**Original Formation String:** `Noun + だけ, Verb-casual + だけ, い-Adjective + だけ, な-Adjective-な + だけ`
- **String Markers:** `だけ`
- **Token Formation Patterns:**
  - [noun] + `だけ`
  - [verb] + `だけ`
  - [adjective] + `だけ`
  - [adjective] + `な` + `だけ`

### Noun に します (Noun ni shimasu)
**Original Formation String:** `Noun + に します`
- **String Markers:** `にします`
- **Token Formation Patterns:**
  - [noun] + `に` + `します`

### Noun に なります (Noun ni narimasu)
**Original Formation String:** `Noun + に + なります`
- **String Markers:** `になります`, `なります`
- **Token Formation Patterns:**
  - [noun] + `に` + `なります`

### Noun に 帰ります (Noun ni kaerimasu)
**Original Formation String:** `Noun + に + 帰ります`
- **String Markers:** `に帰ります`, `帰ります`
- **Token Formation Patterns:**
  - [noun] + `に` + `帰ります`

### Noun に 戻ります (Noun ni modorimasu)
**Original Formation String:** `Noun + に + 戻ります`
- **String Markers:** `に戻ります`, `戻ります`
- **Token Formation Patterns:**
  - [noun] + `に` + `戻ります`

### Noun に 来ます (Noun ni kimasu)
**Original Formation String:** `Noun + に + 来ます (kimasu)`
- **String Markers:** `に来ます`, `来ます`
- **Token Formation Patterns:**
  - [noun] + `に` + `来ます`

### Noun に 行きます (Noun ni ikimasu)
**Original Formation String:** `Noun + に + 行きます`
- **String Markers:** `に行きます`, `行きます`
- **Token Formation Patterns:**
  - [noun] + `に` + `行きます`

### Noun の あとで (Noun no atode)
**Original Formation String:** `Noun + の + あとで`
- **String Markers:** `のあとで`, `あとで`
- **Token Formation Patterns:**
  - [noun] + `の` + `あとで`

### Noun の 前に (Noun no mae ni)
**Original Formation String:** `Noun + の + 前に`
- **String Markers:** `の前に`, `前に`
- **Token Formation Patterns:**
  - [noun] + `の` + `前に`

### Noun や Noun など～ (Noun ya Noun nado)
**Original Formation String:** `Noun1 + や + Noun2 + など`
- **String Markers:** `など`
- **Token Formation Patterns:**
  - [noun] + `や` + [noun] + `など`

### Verb た あとで (ta ato de)
**Original Formation String:** `Verb-た form + あとで`
- **String Markers:** `たあとで`, `あとで`
- **Token Formation Patterns:**
  - [verb] + `あとで`

### Verb たいです (taidesu)
**Original Formation String:** `る-Verb: Remove る and add たいです, う-Verb: Replace the final verb character with the ～い form and add たいです, Exception: する becomes したいです`
- **String Markers:** `たいです`, `したいです`
- **Token Formation Patterns:**
  - [verb] + `る` + `たいです`
  - [verb] + `い` + `たいです` + `する` + `したいです`

### Verb て います (Verb te imasu)
**Original Formation String:** `Verb て-form + います`
- **String Markers:** `ています`, `います`
- **Token Formation Patterns:**
  - [verb] + `て` + `います`

### Verb て ください (Verb-te kudasai)
**Original Formation String:** `Verb-て form + ください`
- **String Markers:** `てください`, `ください`
- **Token Formation Patterns:**
  - [verb] + `ください`

### Verb てから～ (〜te kara)
**Original Formation String:** `Verb-て形 + から`
- **String Markers:** `てから`, `て形`, `から`
- **Token Formation Patterns:**
  - [verb] + `から`

### Verb て～ (Verb + te～)
**Original Formation String:** `Verb (Group 1) - Replace last syllable with 〜て, Verb (Group 2) - Replace 'る' with 〜て, Verb (Group 3) - する becomes して, くる becomes きて`
- **String Markers:** `して`, `くる`, `きて`
- **Token Formation Patterns:**
  - [verb] + `て`
  - [verb] + `る` + `て`
  - [verb] + `する` + `して` + `くる` + `きて`

### Verb ないで ください (〜naide kudasai)
**Original Formation String:** `Verb-ない-form + で ください`
- **String Markers:** `ないでください`, `でください`
- **Token Formation Patterns:**
  - [verb] + `で` + `ください`

### Verb に 来ます (Verb ni kimasu)
**Original Formation String:** `Verb (ます-stem) + に + 来ます`
- **String Markers:** `に来ます`, `来ます`
- **Token Formation Patterns:**
  - [verb] + `に` + `来ます`

### Verb に 行きます (Verb ni ikimasu)
**Original Formation String:** `Verb (ます-stem) + に + 行きます`
- **String Markers:** `に行きます`, `行きます`
- **Token Formation Patterns:**
  - [verb] + `に` + `行きます`

### Verb ましょう (mashou)
**Original Formation String:** `Verb (ます-stem) + ましょう`
- **String Markers:** `ましょう`
- **Token Formation Patterns:**
  - [verb] + `ましょう`

### Verb ましょうか。 (〜mashou ka.)
**Original Formation String:** `Verb (ます-stem) + ましょうか`
- **String Markers:** `ましょうか`
- **Token Formation Patterns:**
  - [verb] + `ましょうか`

### Verb ませんか。 (Verb-masenka)
**Original Formation String:** `Verb (ます-form) + ませんか`
- **String Markers:** `ませんか`
- **Token Formation Patterns:**
  - [verb] + `ませんか`

### Verb る こと が できます (ru koto ga dekimasu)
**Original Formation String:** `Verb (dictionary form) + ことができます`
- **String Markers:** `ることができます`, `ことができます`
- **Token Formation Patterns:**
  - [verb] + `ことができます`

### Verb る こと ができる (ru koto ga dekiru)
**Original Formation String:** `Verb (dictionary form) + ことができる`
- **String Markers:** `ることができる`, `ことができる`
- **Token Formation Patterns:**
  - [verb] + `ことができる`

### Verb る の～ (Verb + ru + no~)
**Original Formation String:** `Verb (dictionary form) + の (casual)`
- **String Markers:** `るの`
- **Token Formation Patterns:**
  - [verb] + `の`

### Verb る 前に (ru mae ni)
**Original Formation String:** `Verb (dictionary form) + 前に`
- **String Markers:** `る前に`, `前に`
- **Token Formation Patterns:**
  - [verb] + `前に`

### Verb ること～ (〜ru koto)
**Original Formation String:** `Verb (dictionary form) + こと`
- **String Markers:** `ること`, `こと`
- **Token Formation Patterns:**
  - [verb] + `こと`

### あまり～ありません (amari ~ arimasen)
**Original Formation String:** `あまり + Verb-ないform + ありません / あまり + い-Adjective-く ありません / あまり + な-Adjective・Noun じゃありません`
- **String Markers:** `あまり`, `ありません`, `くありません`, `じゃありません`
- **Token Formation Patterns:**
  - `あまり` + [verb] + `ありません` + `あまり` + [adjective] + `く` + `ありません` + `あまり` + [adjective] + `・` + [noun] + `じゃありません`

### あまり～ないです (amari ~ nai desu)
**Original Formation String:** `あまり + Verb-ないform + です / あまり + い-Adjective-くない + です / あまり + な-Adjective-じゃない + です`
- **String Markers:** `あまり`, `ないです`, `くない`, `じゃない`
- **Token Formation Patterns:**
  - `あまり` + [verb] + `です` + `あまり` + [adjective] + `くない` + `です` + `あまり` + [adjective] + `じゃない` + `です`

### い-Adjective く します (i-Adjective ku shimasu)
**Original Formation String:** `い-Adjective (remove い) + くします`
- **String Markers:** `くします`
- **Token Formation Patterns:**
  - [adjective] + `くします`

### い-Adjective て (i-Adjective + te~)
**Original Formation String:** `い-Adjective (remove い) + くて + い-Adjective`
- **String Markers:** `くて`
- **Token Formation Patterns:**
  - [adjective] + `くて` + [adjective]

### い-Adjective: Negative Polite Form
**Original Formation String:** `い-Adjective (remove い) + くないです`
- **String Markers:** `くないです`
- **Token Formation Patterns:**
  - [adjective] + `くないです`

### いくつ～ (ikutsu~)
**Original Formation String:** `いくつ + Noun (optional)`
- **String Markers:** `いくつ`
- **Token Formation Patterns:**
  - `いくつ` + [noun]

### いつか～ (itsuka～)
**Original Formation String:** `いつか + sentence`
- **String Markers:** `いつか`
- **Token Formation Patterns:** *None successfully parsed*

### いつでも～ (itsudemo～)
**Original Formation String:** `いつでも + (Verb)`
- **String Markers:** `いつでも`
- **Token Formation Patterns:**
  - `いつでも` + [verb]

### いつも～ (itsumo～)
**Original Formation String:** `いつも + Verb / Adjective / Noun`
- **String Markers:** `いつも`
- **Token Formation Patterns:**
  - `いつも` + [verb] + [adjective] + [noun]

### こちら～ (kochira～)
**Original Formation String:** `こちら / こちら + の + Person/Thing`
- **String Markers:** `こちら`
- **Token Formation Patterns:** *None successfully parsed*

### さっき～ (sakki～)
**Original Formation String:** `さっき + verb / さっき + phrase`
- **String Markers:** `さっき`
- **Token Formation Patterns:** *None successfully parsed*

### すぐに～ (sugu ni～)
**Original Formation String:** `すぐに + Verb/Adjective`
- **String Markers:** `すぐに`
- **Token Formation Patterns:**
  - `すぐに` + [verb] + [adjective]

### ぜんぜん～ (zenzen～)
**Original Formation String:** `ぜんぜん + [Negative verb/adjective]`
- **String Markers:** `ぜんぜん`
- **Token Formation Patterns:** *None successfully parsed*

### そして、～ (soshite、～)
**Original Formation String:** `Sentence 1 + そして + Sentence 2`
- **String Markers:** `そして`
- **Token Formation Patterns:** *None successfully parsed*

### そちら～ (sochira～)
**Original Formation String:** `そちら [alone] / そちら + の + Noun`
- **String Markers:** `そちら`
- **Token Formation Patterns:**
  - `そちら` + `そちら` + `の` + [noun]

### それから、～ (sorekara、～)
**Original Formation String:** `Clause 1 + それから + Clause 2`
- **String Markers:** `それから`
- **Token Formation Patterns:** *None successfully parsed*

### たいてい～ (taitei～)
**Original Formation String:** `たいてい + Verb/い-Adjective/な-Adjective/Noun`
- **String Markers:** `たいてい`
- **Token Formation Patterns:**
  - `たいてい` + [verb] + [adjective] + [adjective] + [noun]

### だいたい〜 (daitai〜)
**Original Formation String:** `だいたい + Number/Amount/Percentage`
- **String Markers:** `だいたい`
- **Token Formation Patterns:** *None successfully parsed*

### だから、～ (dakara、～)
**Original Formation String:** `Noun + だから / な-Adjective + だから`
- **String Markers:** `だから`
- **Token Formation Patterns:**
  - [noun] + `だから` + [adjective] + `だから`

### だれか〜 (dareka〜)
**Original Formation String:** `だれか + Verb, だれか + Adjective, だれか + Noun`
- **String Markers:** `だれか`
- **Token Formation Patterns:**
  - `だれか` + [verb] + `だれか` + [adjective] + `だれか` + [noun]

### だれでも～ (dare demo～)
**Original Formation String:** `だれでも + Verb/Adjective/Noun`
- **String Markers:** `だれでも`
- **Token Formation Patterns:**
  - `だれでも` + [verb] + [adjective] + [noun]

### だれも～ないです (dare mo ~ nai desu)
**Original Formation String:** `だれも + Verb-negative form (ないです), だれも + い-Adjective-negative form (ないです), だれも + な-Adjective-negative form (じゃないです)`
- **String Markers:** `だれも`, `ないです`, `じゃないです`
- **Token Formation Patterns:**
  - `だれも` + [verb] + `だれも` + [adjective] + `だれも` + [adjective]

### だれも～ません (daremo ~masen)
**Original Formation String:** `だれも + Verb-negative (ません)`
- **String Markers:** `だれも`, `ません`
- **Token Formation Patterns:**
  - `だれも` + [verb]

### だれ～ (dare～)
**Original Formation String:** `だれ + appropriate particle (が, は or を)`
- **String Markers:** `だれ`
- **Token Formation Patterns:** *None successfully parsed*

### ときどき～ (tokidoki～)
**Original Formation String:** `ときどき + Verb/Adjective/Noun`
- **String Markers:** `ときどき`
- **Token Formation Patterns:**
  - `ときどき` + [verb] + [adjective] + [noun]

### どうやって～ (douyatte～)
**Original Formation String:** `どうやって + Verb-casual`
- **String Markers:** `どうやって`
- **Token Formation Patterns:**
  - `どうやって` + [verb]

### どこか～ (dokoka～)
**Original Formation String:** `どこか + (Particle, if needed) + Verb/Noun/Adjective`
- **String Markers:** `どこか`
- **Token Formation Patterns:**
  - `どこか` + [verb] + [noun] + [adjective]

### どこでも～ (dokodemo～)
**Original Formation String:** `Simply use the word どこでも in the sentence as an adverb to indicate 'anywhere' or 'everywhere'.`
- **String Markers:** `どこでも`
- **Token Formation Patterns:** *None successfully parsed*

### どこにも + Verb + ないです (doko ni mo + Verb + nai desu)
**Original Formation String:** `どこにも + Verb in ない-form + です`
- **String Markers:** `どこにも`, `ないです`
- **Token Formation Patterns:**
  - `どこにも` + [verb] + `ない` + `です`

### どこにも + Verb + ません (doko ni mo + Verb + masen)
**Original Formation String:** `どこにも + Verb-negative`
- **String Markers:** `どこにも`, `ません`
- **Token Formation Patterns:**
  - `どこにも` + [verb]

### どこへも Verb ないです (doko e mo + Verb + nai desu)
**Original Formation String:** `どこへも + Verb in negative form (ないです)`
- **String Markers:** `どこへも`, `ないです`
- **Token Formation Patterns:**
  - `どこへも` + [verb]

### どこへも Verb ません (doko e mo + Verb + masen)
**Original Formation String:** `どこへも + Verb-negative`
- **String Markers:** `どこへも`, `ません`
- **Token Formation Patterns:**
  - `どこへも` + [verb]

### どこも Verb ないです (dokomo + Verb + naidesu)
**Original Formation String:** `どこも + Verb-negative`
- **String Markers:** `どこも`, `ないです`
- **Token Formation Patterns:**
  - `どこも` + [verb]

### どこも Verb ません (dokomo + Verb + masen)
**Original Formation String:** `どこも + Verb-ます form + ません`
- **String Markers:** `どこも`, `ません`
- **Token Formation Patterns:**
  - `どこも` + [verb] + `ません`

### どこ～ (doko～)
**Original Formation String:** `どこ + question particle`
- **String Markers:** `どこ`
- **Token Formation Patterns:** *None successfully parsed*

### どちら～ (dochira～)
**Original Formation String:** `どちら + が/を + verb, どちら + が/を + adjective, どちら + が/を + noun`
- **String Markers:** `どちら`
- **Token Formation Patterns:** *None successfully parsed*

### どなた～ (donata～)
**Original Formation String:** `どなた`
- **String Markers:** `どなた`
- **Token Formation Patterns:** *None successfully parsed*

### どの Noun (dono Noun)
**Original Formation String:** `どの + Noun`
- **String Markers:** `どの`
- **Token Formation Patterns:**
  - `どの` + [noun]

### どれでも～ (dore demo～)
**Original Formation String:** `どれ + でも`
- **String Markers:** `どれでも`, `どれ`, `でも`
- **Token Formation Patterns:** *None successfully parsed*

### どんな Noun (donna)
**Original Formation String:** `どんな + Noun`
- **String Markers:** `どんな`
- **Token Formation Patterns:**
  - `どんな` + [noun]

### な-Adjective に します (na-Adjective ni shimasu)
**Original Formation String:** `な-Adjective + に + します`
- **String Markers:** `にします`, `します`
- **Token Formation Patterns:**
  - [adjective] + `に` + `します`

### な-Adjective に なります (na-Adjective ni narimasu)
**Original Formation String:** `な-Adjective (remove な) + に + なります`
- **String Markers:** `になります`, `なります`
- **Token Formation Patterns:**
  - [adjective] + `に` + `なります`

### なにか～ (nanika～)
**Original Formation String:** `なにか + Noun`
- **String Markers:** `なにか`
- **Token Formation Patterns:**
  - `なにか` + [noun]

### なにも～ないです (nani mo~nai desu)
**Original Formation String:** `なにも + Verb-negative`
- **String Markers:** `なにも`, `ないです`
- **Token Formation Patterns:**
  - `なにも` + [verb]

### なにも～ません (nanimo~masen)
**Original Formation String:** `なにも + Verb-ます form + ません`
- **String Markers:** `なにも`, `ません`
- **Token Formation Patterns:**
  - `なにも` + [verb] + `ません`

### なに～ (nani~)
**Original Formation String:** `Verb + なに, い-Adjective + なに, な-Adjective + なに, Noun + なに`
- **String Markers:** `なに`
- **Token Formation Patterns:**
  - [verb] + `なに`
  - [adjective] + `なに`
  - [adjective] + `なに`
  - [noun] + `なに`

### なんでも～ (nandemo～)
**Original Formation String:** `なんでも + Verb / なんでも + Adjective / なんでも + Noun`
- **String Markers:** `なんでも`
- **Token Formation Patterns:**
  - `なんでも` + [verb] + `なんでも` + [adjective] + `なんでも` + [noun]

### なんで～ (nande～)
**Original Formation String:** `なんで + [phrase or sentence]`
- **String Markers:** `なんで`
- **Token Formation Patterns:** *None successfully parsed*

### なん～ (nan~)
**Original Formation String:** `なん + Counter / なん + Verb / なん + Adjective`
- **String Markers:** `なん`
- **Token Formation Patterns:**
  - `なん` + `なん` + [verb] + `なん` + [adjective]

### ほとんど〜 (hotondo〜)
**Original Formation String:** `ほとんど + Verb / ほとんど + Noun`
- **String Markers:** `ほとんど`
- **Token Formation Patterns:**
  - `ほとんど` + [verb] + `ほとんど` + [noun]

### まあまあ～ (maa maa～)
**Original Formation String:** `Used as an adverb or short expression with no special grammar structure.`
- **String Markers:** `まあまあ`
- **Token Formation Patterns:** *None successfully parsed*

### まだ〜 (mada〜)
**Original Formation String:** `まだ + Verb (non-past / negative / te-form), まだ + い-adjective, まだ + な-adjective + じゃない/ではない, まだ + Noun + じゃない/ではない`
- **String Markers:** `まだ`, `じゃない`, `ではない`
- **Token Formation Patterns:**
  - `まだ` + [verb] + `まだ` + `い` + `まだ` + `な` + `じゃない` + `ではない` + `まだ` + [noun] + `じゃない` + `ではない`

### まだ〜ないです (mada 〜 nai desu)
**Original Formation String:** `まだ + Verb-negative + です`
- **String Markers:** `まだ`, `ないです`
- **Token Formation Patterns:**
  - `まだ` + [verb] + `です`

### まだ～ません (mada ~masen)
**Original Formation String:** `まだ + Verb-ます form (negative)`
- **String Markers:** `まだ`, `ません`
- **Token Formation Patterns:**
  - `まだ` + [verb]

### もうすぐ〜 (mou sugu~)
**Original Formation String:** `もうすぐ + Verb (~ます form or 〜る form)`
- **String Markers:** `もうすぐ`
- **Token Formation Patterns:**
  - `もうすぐ` + [verb]

### もう～ (mou～)
**Original Formation String:** `もう + Verb / もう + Adjective / もう + Noun`
- **String Markers:** `もう`
- **Token Formation Patterns:**
  - `もう` + [verb] + `もう` + [adjective] + `もう` + [noun]

### もっと〜 (motto〜)
**Original Formation String:** `もっと + Verb / い-Adjective / な-Adjective`
- **String Markers:** `もっと`
- **Token Formation Patterns:**
  - `もっと` + [verb] + [adjective] + [adjective]

### よく～ (yoku ~)
**Original Formation String:** `よく + Verb-casual`
- **String Markers:** `よく`
- **Token Formation Patterns:**
  - `よく` + [verb]

### ～あります (〜arimasu)
**Original Formation String:** `Object + が + あります`
- **String Markers:** `あります`
- **Token Formation Patterns:** *None successfully parsed*

### ～いかがですか。 (〜ikaga desu ka.)
**Original Formation String:** `Noun + は + いかがですか / (Verb-て form + は) いかがですか`
- **String Markers:** `いかがですか`, `はいかがですか`
- **Token Formation Patterns:**
  - [noun] + `は` + `いかがですか` + [verb] + `は` + `いかがですか`

### ～から もらいます (〜kara moraimasu)
**Original Formation String:** `Noun + から + (Verb-て form) + もらいます`
- **String Markers:** `からもらいます`, `から`, `もらいます`
- **Token Formation Patterns:**
  - [noun] + `から` + [verb] + `もらいます`

### ～から、～ (〜kara、～)
**Original Formation String:** `Verb-casual + から / い-Adjective + から / な-Adjective + だから / Noun + だから`
- **String Markers:** `から`, `だから`
- **Token Formation Patterns:**
  - [verb] + `から` + [adjective] + `から` + [adjective] + `だから` + [noun] + `だから`

### ～からです (〜kara desu)
**Original Formation String:** `Verb-casual + からです / い-Adjective + からです / な-Adjective + だからです / Noun + だからです`
- **String Markers:** `からです`, `だからです`
- **Token Formation Patterns:**
  - [verb] + `からです` + [adjective] + `からです` + [adjective] + `だからです` + [noun] + `だからです`

### ～が 私に くれます (〜ga watashi ni kuremasu)
**Original Formation String:** `Person + が + (Thing or Action) + 私に + くれます`
- **String Markers:** `が私にくれます`, `私に`, `くれます`
- **Token Formation Patterns:** *None successfully parsed*

### ～けど、～ (〜kedo、～)
**Original Formation String:** `Verb-casual + けど / い-adjective + けど / な-adjective + だけど / Noun + だけど`
- **String Markers:** `けど`, `だけど`
- **Token Formation Patterns:**
  - [verb] + `けど` + `い` + `けど` + `な` + `だけど` + [noun] + `だけど`

### ～けれど、～ (〜keredo、～)
**Original Formation String:** `Verb-casual + けれど / い-Adjective + けれど / な-Adjective + だけれど / Noun + だけれど`
- **String Markers:** `けれど`, `だけれど`
- **Token Formation Patterns:**
  - [verb] + `けれど` + [adjective] + `けれど` + [adjective] + `だけれど` + [noun] + `だけれど`

### ～たり、～たり します (〜tari, 〜tari shimasu)
**Original Formation String:** `Verb-casual-past + たり + Verb-casual-past + たり + します`
- **String Markers:** `たり`, `たりします`, `します`
- **Token Formation Patterns:**
  - [verb] + `たり` + [verb] + `たり` + `します`

### ～て います (～te imasu)
**Original Formation String:** `Verb て-form + います`
- **String Markers:** `ています`, `います`
- **Token Formation Patterns:**
  - [verb] + `て` + `います`

### ～とき (〜toki)
**Original Formation String:** `Verb-casual + とき / い-Adjective + とき / な-Adjective + なとき / Noun + のとき`
- **String Markers:** `とき`, `なとき`, `のとき`
- **Token Formation Patterns:**
  - [verb] + `とき` + [adjective] + `とき` + [adjective] + `なとき` + [noun] + `のとき`

### ～どう しますか。 (～dou shimasu ka.)
**Original Formation String:** `Situation + どうしますか`
- **String Markers:** `どうしますか`
- **Token Formation Patterns:** *None successfully parsed*

### ～どう 言いますか。 (〜dou iimasu ka.)
**Original Formation String:** `Word/Phrase + は [language]でどう言いますか / Word/Phrase + をどう言いますか`
- **String Markers:** `どう言いますか`, `でどう言いますか`, `をどう言いますか`
- **Token Formation Patterns:** *None successfully parsed*

### ～どうですか。 (〜dou desu ka.)
**Original Formation String:** `Noun + は/が + どうですか / Verb-casual + の + どうですか / い-Adjective + どうですか / な-Adjective + な + どうですか`
- **String Markers:** `どうですか`
- **Token Formation Patterns:**
  - [noun] + `は` + `が` + `どうですか` + [verb] + `の` + `どうですか` + [adjective] + `どうですか` + [adjective] + `な` + `どうですか`

### ～なんと 言いますか。 (〜nan to iimasu ka.)
**Original Formation String:** `Noun + は/が + なんと言いますか`
- **String Markers:** `なんと言いますか`
- **Token Formation Patterns:**
  - [noun] + `は` + `が` + `なんと言いますか`

### ～に あげます (〜 ni agemasu)
**Original Formation String:** `Receiver + に + Object + を + あげます`
- **String Markers:** `にあげます`, `あげます`
- **Token Formation Patterns:** *None successfully parsed*

### ～に もらいます (〜ni moraimasu)
**Original Formation String:** `Giver + に + Verb-te form + もらいます / Giver + に + Object + を + もらいます`
- **String Markers:** `にもらいます`, `もらいます`
- **Token Formation Patterns:**
  - `に` + [verb] + `もらいます` + `に` + `を` + `もらいます`

### ～はたいへんです (〜wa taihen desu)
**Original Formation String:** `Noun + はたいへんです`
- **String Markers:** `はたいへんです`
- **Token Formation Patterns:**
  - [noun] + `はたいへんです`

### ～（場所）に～があります (〜basho ni 〜 ga arimasu)
**Original Formation String:** `Place + に + Object/Thing + が + あります`
- **String Markers:** `場所`, `があります`, `あります`
- **Token Formation Patterns:** *None successfully parsed*

## N4

### A とか B とか
**Original Formation String:** `Noun + とか + Noun + とか`
- **String Markers:** `とか`
- **Token Formation Patterns:**
  - [noun] + `とか` + [noun] + `とか`

### A は B ほど～ありません (A wa B hodo ～ arimasen)
**Original Formation String:** `A は B ほど Verb/adjective ありません`
- **String Markers:** `ほど`, `ありません`
- **Token Formation Patterns:**
  - `は` + `ほど` + [verb] + `ありません`

### A は B ほど～ない (A wa B hodo ~ nai)
**Original Formation String:** `A は B ほど + い-Adjective stem (without い) + くない, な-Adjective + じゃない, Verb-negative potential form`
- **String Markers:** `ほど`, `くない`, `じゃない`
- **Token Formation Patterns:**
  - `は` + `ほど` + [adjective] + `くない`
  - [adjective] + `じゃない`

### A より B のほうが〜 (A yori B no hou ga 〜)
**Original Formation String:** `A + より + B + のほうが + Adjective/Verb`
- **String Markers:** `より`, `のほうが`
- **Token Formation Patterns:**
  - `より` + `のほうが` + [adjective] + [verb]

### Noun + 中 (Noun + ちゅう)
**Original Formation String:** `Noun + 中 (ちゅう)`
- **String Markers:** `ちゅう`, `中ちゅう`
- **Token Formation Patterns:**
  - [noun] + `中`

### Noun しか～ない (Noun shika~nai)
**Original Formation String:** `Noun + しか + Negative Verb`
- **String Markers:** `しか`
- **Token Formation Patterns:**
  - [noun] + `しか` + [verb]

### Noun に する (Noun ni suru)
**Original Formation String:** `Noun + に + する`
- **String Markers:** `にする`
- **Token Formation Patterns:**
  - [noun] + `に` + `する`

### Noun に なる (Noun ni naru)
**Original Formation String:** `Noun + に + なる`
- **String Markers:** `になる`
- **Token Formation Patterns:**
  - [noun] + `に` + `なる`

### Noun の 間に (〜no aida ni)
**Original Formation String:** `Noun + の間に`
- **String Markers:** `の間に`
- **Token Formation Patterns:**
  - [noun] + `の間に`

### Noun ばかり (〜bakari)
**Original Formation String:** `Noun + ばかり, Verb-casual + ばかり, い-Adjective + ばかり, な-Adjective + だ ばかり`
- **String Markers:** `ばかり`, `だばかり`
- **Token Formation Patterns:**
  - [noun] + `ばかり`
  - [verb] + `ばかり`
  - [adjective] + `ばかり`
  - [adjective] + `だ` + `ばかり`

### Noun もらう (Noun wo morau)
**Original Formation String:** `Noun + を + もらう`
- **String Markers:** `もらう`
- **Token Formation Patterns:**
  - [noun] + `を` + `もらう`

### Noun を あげる (Noun wo ageru)
**Original Formation String:** `Noun + を + あげる`
- **String Markers:** `をあげる`, `あげる`
- **Token Formation Patterns:**
  - [noun] + `を` + `あげる`

### Noun を くれる (Noun wo kureru)
**Original Formation String:** `Giver + が + Receiver + に + Noun + を + くれる`
- **String Markers:** `をくれる`, `くれる`
- **Token Formation Patterns:**
  - `が` + `に` + [noun] + `を` + `くれる`

### Noun を さしあげる (Noun wo sashiageru)
**Original Formation String:** `Noun + を + さしあげる`
- **String Markers:** `をさしあげる`, `さしあげる`
- **Token Formation Patterns:**
  - [noun] + `を` + `さしあげる`

### Nounをいただく (Noun wo itadaku)
**Original Formation String:** `Noun + を + いただく`
- **String Markers:** `をいただく`, `いただく`
- **Token Formation Patterns:**
  - [noun] + `を` + `いただく`

### Nounをくださる
**Original Formation String:** `Noun + を + くださる`
- **String Markers:** `をくださる`, `くださる`
- **Token Formation Patterns:**
  - [noun] + `を` + `くださる`

### Verb + 続ける (つづける, tsuzukeru)
**Original Formation String:** `Verb-masu-stem + 続ける`
- **String Markers:** `続けるつづける`, `続ける`
- **Token Formation Patterns:**
  - [verb] + `続ける`

### Verb させられる (Verb-saserareru)
**Original Formation String:** `Group 1 Verb: Replace ～う with ～わせられる, Group 2 Verb: Replace ～る with ～させられる, Group 3 Verb: する → させられる, くる → こさせられる`
- **String Markers:** `させられる`, `わせられる`, `くる`, `こさせられる`
- **Token Formation Patterns:**
  - [verb] + `う` + `わせられる` + [verb] + `る` + `させられる` + [verb] + `する` + `させられる` + `くる` + `こさせられる`

### Verb させる (Verb-saseru)
**Original Formation String:** `Group 1 Verbs: Change the last hiragana to ～せる, Group 2 Verbs: Remove ～る and add ～させる, Group 3 Verbs: する → させる, くる → こさせる`
- **String Markers:** `させる`, `せる`, `くる`, `こさせる`
- **Token Formation Patterns:**
  - [verb] + `せる` + [verb] + `る` + `させる` + [verb] + `する` + `させる` + `くる` + `こさせる`

### Verb た ことがある (Verb ta koto ga aru)
**Original Formation String:** `Verb-た-form + ことがある`
- **String Markers:** `たことがある`, `ことがある`
- **Token Formation Patterns:**
  - [verb] + `ことがある`

### Verb た ときに (Verb た ときに)
**Original Formation String:** `Verb-た + ときに`
- **String Markers:** `たときに`, `ときに`
- **Token Formation Patterns:**
  - [verb] + `ときに`

### Verb た ところ (Verb ta tokoro)
**Original Formation String:** `Verb (た form) + ところ`
- **String Markers:** `たところ`, `ところ`
- **Token Formation Patterns:**
  - [verb] + `ところ`

### Verb たほうがいい (〜ta hou ga ii)
**Original Formation String:** `Verb (past tense) + ほうがいい`
- **String Markers:** `たほうがいい`, `ほうがいい`
- **Token Formation Patterns:**
  - [verb] + `ほうがいい`

### Verb ために (tame ni)
**Original Formation String:** `1) Verb (dictionary form) + ために (purpose)
2) い-Adjective + ために (reason)
3) な-Adjective + な + ために (reason)
4) Noun + の + ために (reason)`
- **String Markers:** `ために`
- **Token Formation Patterns:**
  - [verb] + `ために` + [adjective] + `ために` + [adjective] + `な` + `ために` + [noun] + `の` + `ために`

### Verb つもり (〜tsumori)
**Original Formation String:** `Verb-casual + つもり`
- **String Markers:** `つもり`
- **Token Formation Patterns:**
  - [verb] + `つもり`

### Verb て + さしあげる (Verb TE sashiageru)
**Original Formation String:** `Verb-てform + さしあげる`
- **String Markers:** `さしあげる`
- **Token Formation Patterns:**
  - [verb] + `さしあげる`

### Verb て ある (Verb-te aru)
**Original Formation String:** `Verb-て form + ある`
- **String Markers:** `てある`
- **Token Formation Patterns:**
  - [verb] + `ある`

### Verb て いく (Verb-te iku)
**Original Formation String:** `Verb in て-form + いく`
- **String Markers:** `ていく`, `いく`
- **Token Formation Patterns:**
  - [verb] + `て` + `いく`

### Verb て いただけませんか (Verb te itadakemasen ka)
**Original Formation String:** `Verb-て form + いただけませんか`
- **String Markers:** `ていただけませんか`, `いただけませんか`
- **Token Formation Patterns:**
  - [verb] + `いただけませんか`

### Verb て いる (Verb-te iru)
**Original Formation String:** `Verb (て-form) + いる`
- **String Markers:** `ている`
- **Token Formation Patterns:**
  - [verb] + `いる`

### Verb て いる ところ (Verb te iru tokoro)
**Original Formation String:** `Verb-て form + いる ところ`
- **String Markers:** `ているところ`, `いるところ`
- **Token Formation Patterns:**
  - [verb] + `いる` + `ところ`

### Verb て くださいませんか (Verb-te kudasaimasen ka)
**Original Formation String:** `Verb in て-form + くださいませんか`
- **String Markers:** `てくださいませんか`, `くださいませんか`
- **Token Formation Patterns:**
  - [verb] + `て` + `くださいませんか`

### Verb て くださる (Verb-te kudasaru)
**Original Formation String:** `Verb て-form + くださる`
- **String Markers:** `てくださる`, `くださる`
- **Token Formation Patterns:**
  - [verb] + `て` + `くださる`

### Verb て くる (Verb te kuru)
**Original Formation String:** `Verb て-form + くる`
- **String Markers:** `てくる`, `くる`
- **Token Formation Patterns:**
  - [verb] + `て` + `くる`

### Verb て くれる (Verb-te kureru)
**Original Formation String:** `Verb-te form + くれる`
- **String Markers:** `てくれる`, `くれる`
- **Token Formation Patterns:**
  - [verb] + `くれる`

### Verb て ほしい (Verb-te hoshii)
**Original Formation String:** `Verb-て form + ほしい`
- **String Markers:** `てほしい`, `ほしい`
- **Token Formation Patterns:**
  - [verb] + `ほしい`

### Verb て もらう (Verb-te morau)
**Original Formation String:** `Verb-て form + もらう`
- **String Markers:** `てもらう`, `もらう`
- **Token Formation Patterns:**
  - [verb] + `もらう`

### Verb てあげる (Verb te ageru)
**Original Formation String:** `Verb-て form + あげる`
- **String Markers:** `てあげる`, `あげる`
- **Token Formation Patterns:**
  - [verb] + `あげる`

### Verb ていただきたい (te itadakitai)
**Original Formation String:** `Verb-て form + いただきたい`
- **String Markers:** `ていただきたい`, `いただきたい`
- **Token Formation Patterns:**
  - [verb] + `いただきたい`

### Verb ていただく (〜te itadaku)
**Original Formation String:** `Verb-て form + いただく`
- **String Markers:** `ていただく`, `いただく`
- **Token Formation Patterns:**
  - [verb] + `いただく`

### Verb ている間に (te iru aida ni)
**Original Formation String:** `Verb-て form + いる + 間に`
- **String Markers:** `ている間に`, `間に`
- **Token Formation Patterns:**
  - [verb] + `いる` + `間に`

### Verb ておく (〜te oku)
**Original Formation String:** `Verb-て form + おく`
- **String Markers:** `ておく`, `おく`
- **Token Formation Patterns:**
  - [verb] + `おく`

### Verb てくれませんか (〜te kuremasen ka)
**Original Formation String:** `Verb-て form + くれませんか`
- **String Markers:** `てくれませんか`, `くれませんか`
- **Token Formation Patterns:**
  - [verb] + `くれませんか`

### Verb てしまう (〜te shimau)
**Original Formation String:** `Verb-te form + しまう`
- **String Markers:** `てしまう`, `しまう`
- **Token Formation Patterns:**
  - [verb] + `しまう`

### Verb てみる (〜te miru)
**Original Formation String:** `Verb-て form + みる`
- **String Markers:** `てみる`, `みる`
- **Token Formation Patterns:**
  - [verb] + `みる`

### Verb てもらいたい (～te moraitai)
**Original Formation String:** `Verb-て-form + もらいたい`
- **String Markers:** `てもらいたい`, `もらいたい`
- **Token Formation Patterns:**
  - [verb] + `もらいたい`

### Verb てもらえませんか (～te moraemasen ka)
**Original Formation String:** `Verb-て form + もらえませんか`
- **String Markers:** `てもらえませんか`, `もらえませんか`
- **Token Formation Patterns:**
  - [verb] + `もらえませんか`

### Verb ない + ことにする (Verb nai koto ni suru)
**Original Formation String:** `Verb-ない form + ことにする`
- **String Markers:** `ことにする`
- **Token Formation Patterns:**
  - [verb] + `ことにする`

### Verb ない ことがある (Verb-nai koto ga aru)
**Original Formation String:** `Verb-negative form + ことがある`
- **String Markers:** `ないことがある`, `ことがある`
- **Token Formation Patterns:**
  - [verb] + `ことがある`

### Verb ない ことになる (Verb nai koto ni naru)
**Original Formation String:** `Verb-negative (ない) + ことになる`
- **String Markers:** `ないことになる`, `ことになる`
- **Token Formation Patterns:**
  - [verb] + `ことになる`

### Verb ないほうがいい (Verb nai hou ga ii)
**Original Formation String:** `Verb-negative form + ほうがいい`
- **String Markers:** `ないほうがいい`, `ほうがいい`
- **Token Formation Patterns:**
  - [verb] + `ほうがいい`

### Verb ながら (〜nagara)
**Original Formation String:** `Verb-masu stem + ながら`
- **String Markers:** `ながら`
- **Token Formation Patterns:**
  - [verb] + `ながら`

### Verb なさい (〜nasai)
**Original Formation String:** `Verb-stem + なさい`
- **String Markers:** `なさい`
- **Token Formation Patterns:**
  - [verb] + `なさい`

### Verb にくい (〜nikui)
**Original Formation String:** `Verb-stem + にくい`
- **String Markers:** `にくい`
- **Token Formation Patterns:**
  - [verb] + `にくい`

### Verb やすい (〜yasui)
**Original Formation String:** `Verb-stem + やすい`
- **String Markers:** `やすい`
- **Token Formation Patterns:**
  - [verb] + `やすい`

### Verb ようと思う (Verb-you to omou)
**Original Formation String:** `Verb-volitional + と思う`
- **String Markers:** `ようと思う`, `と思う`
- **Token Formation Patterns:**
  - [verb] + `と思う`

### Verb ように (〜you ni)
**Original Formation String:** `Examples: Noun + のように / Verb-casual + ように / い-adjective + ように`
- **String Markers:** `ように`, `のように`
- **Token Formation Patterns:**
  - [noun] + `のように` + [verb] + `ように` + `い` + `ように`

### Verb ようにする (Verb ~you ni suru)
**Original Formation String:** `Verb-dictionary form + ようにする`
- **String Markers:** `ようにする`
- **Token Formation Patterns:**
  - [verb] + `ようにする`

### Verb ようになる (〜you ni naru)
**Original Formation String:** `Verb-dictionary/potential form + ようになる`
- **String Markers:** `ようになる`
- **Token Formation Patterns:**
  - [verb] + `ようになる`

### Verb ように言う (Verb-you ni iu)
**Original Formation String:** `Verb-casual + ように言う`
- **String Markers:** `ように言う`
- **Token Formation Patterns:**
  - [verb] + `ように言う`

### Verb られる (〜rareru)
**Original Formation String:** `う-verb (passive): Replace the final う with われる / る-verb (passive & potential): Replace る with られる / Irregular: する → される, くる → こられる`
- **String Markers:** `られる`, `われる`, `される`, `くる`
- **Token Formation Patterns:** *None successfully parsed*

### Verb る ことがある (〜ru koto ga aru)
**Original Formation String:** `Verb-dictionary form + ことがある`
- **String Markers:** `ることがある`, `ことがある`
- **Token Formation Patterns:**
  - [verb] + `ことがある`

### Verb る ことになる (〜ru koto ni naru)
**Original Formation String:** `Verb-る + ことになる`
- **String Markers:** `ることになる`, `ことになる`
- **Token Formation Patterns:**
  - [verb] + `ことになる`

### Verb る ところ (Verb-ru tokoro)
**Original Formation String:** `Verb-dictionary form + ところ`
- **String Markers:** `るところ`, `ところ`
- **Token Formation Patterns:**
  - [verb] + `ところ`

### Verb ることができる (〜ru koto ga dekiru)
**Original Formation String:** `Verb-る + ことができる`
- **String Markers:** `ることができる`, `ことができる`
- **Token Formation Patterns:**
  - [verb] + `ことができる`

### Verb ることにする (〜ru koto ni suru)
**Original Formation String:** `Verb-る + ことにする`
- **String Markers:** `ることにする`, `ことにする`
- **Token Formation Patterns:**
  - [verb] + `ことにする`

### Verb るときに (〜ru toki ni)
**Original Formation String:** `Verb-る + ときに`
- **String Markers:** `るときに`, `ときに`
- **Token Formation Patterns:**
  - [verb] + `ときに`

### Verb 出す (~dasu)
**Original Formation String:** `Verb stem + 出す (~dasu)`
- **String Markers:** `出す`
- **Token Formation Patterns:**
  - [verb] + `出す`

### Verb 方 (〜hou)
**Original Formation String:** `Verb-stem + 方 (read as かた)`
- **String Markers:** `かた`
- **Token Formation Patterns:**
  - [verb] + `方`

### Verb 終わる (〜owaru)
**Original Formation String:** `終わる (owaru) is a godan (u-verb)`
- **String Markers:** `終わる`
- **Token Formation Patterns:** *None successfully parsed*

### い-Adjective く する/なる (i-Adjective kusuru/naru)
**Original Formation String:** `い-Adjective (remove い) + く + する/なる`
- **String Markers:** `くする`
- **Token Formation Patterns:**
  - [adjective] + `く` + `する` + `なる`

### そんな (sonna) + Noun
**Original Formation String:** `そんな + Noun`
- **String Markers:** `そんな`
- **Token Formation Patterns:**
  - `そんな` + [noun]

### そんなに～ (sonna ni〜)
**Original Formation String:** `そんなに + Verb-negation, そんなに + Adjective-negation`
- **String Markers:** `そんなに`
- **Token Formation Patterns:**
  - `そんなに` + [verb] + `そんなに` + [adjective]

### どういう Noun (dou iu Noun)
**Original Formation String:** `どういう + Noun`
- **String Markers:** `どういう`
- **Token Formation Patterns:**
  - `どういう` + [noun]

### な-adjective に する/なる
**Original Formation String:** `な-Adjective + に + する/なる`
- **String Markers:** `にする`
- **Token Formation Patterns:**
  - [adjective] + `に` + `する` + `なる`

### のために (no tame ni)
**Original Formation String:** `Noun + のために`
- **String Markers:** `のために`
- **Token Formation Patterns:**
  - [noun] + `のために`

### 文A。そのうえ 文B。
**Original Formation String:** `Sentence A + そのうえ + Sentence B + 。`
- **String Markers:** `そのうえ文`, `そのうえ`
- **Token Formation Patterns:** *None successfully parsed*

### 文A。それで 文B (Bun A. Sorede Bun B)
**Original Formation String:** `Sentence A。それで Sentence B。`
- **String Markers:** `それで文`, `それで`
- **Token Formation Patterns:** *None successfully parsed*

### 文A。それに 文B (Bun A. Soreni Bun B)
**Original Formation String:** `Sentence A + それに + Sentence B`
- **String Markers:** `それに文`, `それに`
- **Token Formation Patterns:** *None successfully parsed*

### 文A。だから 文B (Bun A. Dakara Bun B)
**Original Formation String:** `Sentence A + だから + Sentence B`
- **String Markers:** `だから文`, `だから`
- **Token Formation Patterns:** *None successfully parsed*

### ～かしら (〜kashira)
**Original Formation String:** `Verb-casual + かしら, い-Adjective + かしら, な-Adjective + かしら, Noun + かしら`
- **String Markers:** `かしら`
- **Token Formation Patterns:**
  - [verb] + `かしら`
  - [adjective] + `かしら`
  - [adjective] + `かしら`
  - [noun] + `かしら`

### ～かどうか (〜ka dou ka)
**Original Formation String:** `Verb-casual + かどうか, い-Adjective + かどうか, な-Adjective + (だ)かどうか, Noun + (だ)かどうか`
- **String Markers:** `かどうか`, `だかどうか`
- **Token Formation Patterns:**
  - [verb] + `かどうか`
  - [adjective] + `かどうか`
  - [adjective] + `かどうか`
  - [noun] + `かどうか`

### ～かなあ (〜kanaa)
**Original Formation String:** `Verb-casual + かなあ, い-Adjective + かなあ, (な-Adjective/Noun) + (だ) + かなあ`
- **String Markers:** `かなあ`
- **Token Formation Patterns:**
  - [verb] + `かなあ`
  - [adjective] + `かなあ` + [adjective] + [noun] + `かなあ`

### ～かもしれない (〜kamoshirenai)
**Original Formation String:** `Verb-casual + かもしれない, い-Adjective + かもしれない, な-Adjective + だかもしれない, Noun + だかもしれない`
- **String Markers:** `かもしれない`, `だかもしれない`
- **Token Formation Patterns:**
  - [verb] + `かもしれない`
  - [adjective] + `かもしれない`
  - [adjective] + `だかもしれない`
  - [noun] + `だかもしれない`

### ～から (〜kara)
**Original Formation String:** `Verb-casual + から, い-Adjective + から, な-Adjective + だから, Noun + だから`
- **String Markers:** `から`, `だから`
- **Token Formation Patterns:**
  - [verb] + `から`
  - [adjective] + `から`
  - [adjective] + `だから`
  - [noun] + `だから`

### ～けれど (〜keredo)
**Original Formation String:** `Verb-casual + けれど, い-Adjective + けれど, な-Adjective + だけれど, Noun + だけれど`
- **String Markers:** `けれど`, `だけれど`
- **Token Formation Patterns:**
  - [verb] + `けれど`
  - [adjective] + `けれど`
  - [adjective] + `だけれど`
  - [noun] + `だけれど`

### ～させてください (〜sasete kudasai)
**Original Formation String:** `Verb-causative form + ください`
- **String Markers:** `させてください`, `ください`
- **Token Formation Patterns:**
  - [verb] + `ください`

### ～し、～し、～ (〜shi, 〜shi, 〜)
**Original Formation String:** `Verb-casual + し, い-Adjective + し, な-Adjective + だし, Noun + だし`
- **String Markers:** `だし`
- **Token Formation Patterns:**
  - [verb] + `し`
  - [adjective] + `し`
  - [adjective] + `だし`
  - [noun] + `だし`

### ～すぎる (〜sugiru)
**Original Formation String:** `Verb-stem + すぎる, い-Adjective (remove い) + すぎる, な-Adjective + すぎる`
- **String Markers:** `すぎる`
- **Token Formation Patterns:**
  - [verb] + `すぎる`
  - [adjective] + `すぎる`
  - [adjective] + `すぎる`

### ～ずつ (〜zutsu)
**Original Formation String:** `Noun + ずつ`
- **String Markers:** `ずつ`
- **Token Formation Patterns:**
  - [noun] + `ずつ`

### ～そうだ (〜sou da)
**Original Formation String:** `Verb-ますstem + そうだ, い-Adjective (without い) + そうだ, な-Adjective + そうだ`
- **String Markers:** `そうだ`
- **Token Formation Patterns:**
  - [verb] + `そうだ`
  - [adjective] + `そうだ`
  - [adjective] + `そうだ`

### ～たら いかがですか (〜tara ikaga desu ka)
**Original Formation String:** `Verb-casual, past + たら いかがですか, い-Adjective + かったら いかがですか, な-Adjective + だったら いかがですか, Noun + だったら いかがですか`
- **String Markers:** `たらいかがですか`, `かったらいかがですか`, `だったらいかがですか`
- **Token Formation Patterns:**
  - [verb] + `たら` + `いかがですか`
  - [adjective] + `かったら` + `いかがですか`
  - [adjective] + `だったら` + `いかがですか`
  - [noun] + `だったら` + `いかがですか`

### ～たら どうですか (〜tara doudesuka)
**Original Formation String:** `Verb-た form + ら どうですか`
- **String Markers:** `たらどうですか`, `らどうですか`
- **Token Formation Patterns:**
  - [verb] + `ら` + `どうですか`

### ～たらいい (〜tara ii)
**Original Formation String:** `Verb-casual-past + たらいい`
- **String Markers:** `たらいい`
- **Token Formation Patterns:**
  - [verb] + `たらいい`

### ～たり～たり (〜tari 〜tari)
**Original Formation String:** `Verb-ta + り + next verb-ta + り, い-Adjective + かったり + next verb-ta + り, な-Adjective + だったり + next verb-ta + り, Noun + だったり + next verb-ta + り`
- **String Markers:** `たり`, `かったり`, `だったり`
- **Token Formation Patterns:**
  - [verb] + `り` + `り`
  - [adjective] + `かったり` + `り`
  - [adjective] + `だったり` + `り`
  - [noun] + `だったり` + `り`

### ～だろう (〜darou)
**Original Formation String:** `Verb-casual + だろう, い-Adjective (drop い) + だろう, な-Adjective + だろう, Noun + だろう`
- **String Markers:** `だろう`
- **Token Formation Patterns:**
  - [verb] + `だろう`
  - [adjective] + `だろう`
  - [adjective] + `だろう`
  - [noun] + `だろう`

### ～っていう (〜tte iu)
**Original Formation String:** `Noun/Adjective/Verb + っていう + Noun`
- **String Markers:** `っていう`
- **Token Formation Patterns:**
  - [noun] + [adjective] + [verb] + `っていう` + [noun]

### ～てはいけない (〜te wa ikenai)
**Original Formation String:** `Verb-て-form + はいけない`
- **String Markers:** `てはいけない`, `はいけない`
- **Token Formation Patterns:**
  - [verb] + `はいけない`

### ～ても/でも (〜te mo/demo)
**Original Formation String:** `Verb-て-form + も, い-Adjective (-い) + くても, な-Adjective + でも, Noun + でも`
- **String Markers:** `ても`, `でも`, `くても`
- **Token Formation Patterns:**
  - [verb] + `も`
  - [adjective] + `くても`
  - [adjective] + `でも`
  - [noun] + `でも`

### ～てもいい (〜temo ii)
**Original Formation String:** `Verb-て form + もいい`
- **String Markers:** `てもいい`, `もいい`
- **Token Formation Patterns:**
  - [verb] + `もいい`

### ～でしょう (〜deshou)
**Original Formation String:** `Verb-ますstem + でしょう, い-Adjective + でしょう, な-Adjective + でしょう, Noun + でしょう`
- **String Markers:** `でしょう`
- **Token Formation Patterns:**
  - [verb] + `でしょう`
  - [adjective] + `でしょう`
  - [adjective] + `でしょう`
  - [noun] + `でしょう`

### ～といい (〜to ii)
**Original Formation String:** `Verb-casual + といい, い-Adjective + といい, な-Adjective + だといい, Noun + だといい`
- **String Markers:** `といい`, `だといい`
- **Token Formation Patterns:**
  - [verb] + `といい`
  - [adjective] + `といい`
  - [adjective] + `だといい`
  - [noun] + `だといい`

### ～という (〜to iu)
**Original Formation String:** `Verb-casual + という, い-Adjective + という, な-Adjective + という, Noun + という`
- **String Markers:** `という`
- **Token Formation Patterns:**
  - [verb] + `という`
  - [adjective] + `という`
  - [adjective] + `という`
  - [noun] + `という`

### ～という (〜to iu) Noun
**Original Formation String:** `Noun + という + Noun, な-Adjective + という + Noun, Adjectival Verb + という + Noun`
- **String Markers:** `という`
- **Token Formation Patterns:**
  - [noun] + `という` + [noun]
  - [adjective] + `という` + [noun] + [verb] + `という` + [noun]

### ～と思う (〜to omou)
**Original Formation String:** `Verb-casual + と思う, い-Adjective + と思う, な-Adjective + だと思う, Noun + だと思う`
- **String Markers:** `と思う`, `だと思う`
- **Token Formation Patterns:**
  - [verb] + `と思う`
  - [adjective] + `と思う`
  - [adjective] + `だと思う`
  - [noun] + `だと思う`

### ～ないといけない (〜nai to ikenai)
**Original Formation String:** `Verb-negative + といけない`
- **String Markers:** `ないといけない`, `といけない`
- **Token Formation Patterns:**
  - [verb] + `といけない`

### ～なきゃいけない (〜nakya ikenai)
**Original Formation String:** `Verb-casual (negative form without い) + なきゃいけない`
- **String Markers:** `なきゃいけない`
- **Token Formation Patterns:**
  - [verb] + `なきゃいけない`

### ～なくちゃいけない (〜naku cha ikenai)
**Original Formation String:** `Verb-ない form (-ない ending is dropped) + なくちゃいけない`
- **String Markers:** `なくちゃいけない`
- **Token Formation Patterns:**
  - [verb] + `なくちゃいけない`

### ～なくてはいけない (〜nakute wa ikenai)
**Original Formation String:** `Verb-negative form + なくてはいけない`
- **String Markers:** `なくてはいけない`
- **Token Formation Patterns:**
  - [verb] + `なくてはいけない`

### ～なくてもいい (〜nakutemo ii)
**Original Formation String:** `Verb-ない-form + てもいい`
- **String Markers:** `なくてもいい`, `てもいい`
- **Token Formation Patterns:**
  - [verb] + `てもいい`

### ～なければ ならない (〜nakereba naranai)
**Original Formation String:** `Verb-ない form + なければ ならない`
- **String Markers:** `なければならない`
- **Token Formation Patterns:**
  - [verb] + `なければ` + `ならない`

### ～ので (〜node)
**Original Formation String:** `Verb-casual + ので, い-Adjective + ので, な-Adjective + なので, Noun + なので`
- **String Markers:** `ので`, `なので`
- **Token Formation Patterns:**
  - [verb] + `ので`
  - [adjective] + `ので`
  - [adjective] + `なので`
  - [noun] + `なので`

### ～のです (〜no desu)
**Original Formation String:** `Verb-casual + のです, い-Adjective + のです, な-Adjective + なのです, Noun + なのです`
- **String Markers:** `のです`, `なのです`
- **Token Formation Patterns:**
  - [verb] + `のです`
  - [adjective] + `のです`
  - [adjective] + `なのです`
  - [noun] + `なのです`

### ～のに (〜no ni)
**Original Formation String:** `Verb-casual + のに, い-Adjective + のに, な-Adjective + なのに, Noun + なのに`
- **String Markers:** `のに`, `なのに`
- **Token Formation Patterns:**
  - [verb] + `のに`
  - [adjective] + `のに`
  - [adjective] + `なのに`
  - [noun] + `なのに`

### ～ばいい (〜ba ii)
**Original Formation String:** `Verb-ば-form + いい, い-Adjective + ければいい, な-Adjective + であればいい, Noun + であればいい`
- **String Markers:** `ばいい`, `いい`, `ければいい`, `であればいい`
- **Token Formation Patterns:**
  - [verb] + `いい`
  - [adjective] + `ければいい`
  - [adjective] + `であればいい`
  - [noun] + `であればいい`

### ～まで (〜made)
**Original Formation String:** `Verb + まで, い-Adjective + まで, な-Adjective + まで, Noun + まで`
- **String Markers:** `まで`
- **Token Formation Patterns:**
  - [verb] + `まで`
  - [adjective] + `まで`
  - [adjective] + `まで`
  - [noun] + `まで`

### ～までに (〜made ni)
**Original Formation String:** `Verb-casual + までに, Noun + までに, Time expression + までに`
- **String Markers:** `までに`
- **Token Formation Patterns:**
  - [verb] + `までに`
  - [noun] + `までに` + `までに`

### ～まま (〜mama)
**Original Formation String:** `Verb-てform + いる+ まま, Adjective (い & な) + まま, Noun + のまま`
- **String Markers:** `まま`, `のまま`
- **Token Formation Patterns:**
  - [verb] + `いる` + `まま`
  - [adjective] + `まま`
  - [noun] + `のまま`

### ～みたいだ (〜mitai da)
**Original Formation String:** `Verb-casual + みたいだ, い-Adjective + みたいだ, な-Adjective + みたいだ, Noun + みたいだ`
- **String Markers:** `みたいだ`
- **Token Formation Patterns:**
  - [verb] + `みたいだ`
  - [adjective] + `みたいだ`
  - [adjective] + `みたいだ`
  - [noun] + `みたいだ`

### ～ようだ (〜you da)
**Original Formation String:** `Verb-て form + ようだ, い-Adjective (drop い) + ようだ, な-Adjective + のようだ, Noun + のようだ`
- **String Markers:** `ようだ`, `のようだ`
- **Token Formation Patterns:**
  - [verb] + `ようだ`
  - [adjective] + `ようだ`
  - [adjective] + `のようだ`
  - [noun] + `のようだ`

### ～んです (〜n desu)
**Original Formation String:** `Verb-casual + んです, い-Adjective + んです, な-Adjective + なんです, Noun + なんです`
- **String Markers:** `んです`, `なんです`
- **Token Formation Patterns:**
  - [verb] + `んです`
  - [adjective] + `んです`
  - [adjective] + `なんです`
  - [noun] + `なんです`

## N3

### A その上 B (A sono ue B)
**Original Formation String:** `A [sentence/clause] + その上 + B [sentence/clause]`
- **String Markers:** `その上`
- **Token Formation Patterns:** *None successfully parsed*

### すこしも〜ない (sukoshimo~nai)
**Original Formation String:** `すこしも + Verb-negative`
- **String Markers:** `すこしも`
- **Token Formation Patterns:**
  - `すこしも` + [verb]

### だけど (dakedo)
**Original Formation String:** `Sentence 1 + だけど + Sentence 2, or Sentence 1 + 。だけど、Sentence 2`
- **String Markers:** `だけど`
- **Token Formation Patterns:** *None successfully parsed*

### ですから～ (desu kara)
**Original Formation String:** `Sentence A + ですから + Sentence B`
- **String Markers:** `ですから`
- **Token Formation Patterns:** *None successfully parsed*

### ところで (tokorode)
**Original Formation String:** `ところで + new topic or question`
- **String Markers:** `ところで`
- **Token Formation Patterns:** *None successfully parsed*

### どんなに～ても (donna ni ~ temo)
**Original Formation String:** `どんなに + Verb-てform + も, どんなに + い-Adjective-てform + も, どんなに + な-Adjective + でも`
- **String Markers:** `どんなに`, `ても`, `でも`
- **Token Formation Patterns:**
  - `どんなに` + [verb] + `も` + `どんなに` + [adjective] + `て` + `も` + `どんなに` + [adjective] + `でも`

### まったく～ない (mattaku ~nai)
**Original Formation String:** `まったく + Verb-negative, まったく + い-Adjective-negative, まったく + な-Adjective-negative`
- **String Markers:** `まったく`
- **Token Formation Patterns:**
  - `まったく` + [verb] + `まったく` + [adjective] + `まったく` + [adjective]

### まるで～よう (maru de ~ you)
**Original Formation String:** `まるで + phrase/sentence + よう`
- **String Markers:** `まるで`, `よう`
- **Token Formation Patterns:** *None successfully parsed*

### もしかすると〜かもしれない (moshikasuru to 〜kamoshirenai)
**Original Formation String:** `もしかすると + Sentence + かもしれない`
- **String Markers:** `もしかすると`, `かもしれない`
- **Token Formation Patterns:** *None successfully parsed*

### もしも～なら (moshimo ~ nara)
**Original Formation String:** `Verb-casual + なら, い-Adjective + なら, な-Adjective + なら, Noun + なら`
- **String Markers:** `もしも`, `なら`
- **Token Formation Patterns:**
  - [verb] + `なら`
  - [adjective] + `なら`
  - [adjective] + `なら`
  - [noun] + `なら`

### もし～たなら (moshi ~ tanara)
**Original Formation String:** `もし + Verb-casual past + なら, もし + い-Adjective-casual past + なら, もし + な-Adjective + だったなら, もし + Noun + だったなら`
- **String Markers:** `もし`, `たなら`, `なら`, `だったなら`
- **Token Formation Patterns:**
  - `もし` + [verb] + `なら` + `もし` + [adjective] + `なら` + `もし` + [adjective] + `だったなら` + `もし` + [noun] + `だったなら`

### もし～ても (moshi ~ temo)
**Original Formation String:** `もし + Verb-て form + も / もし + い-Adjective(く) + ても / もし + な-Adjective/Noun + でも`
- **String Markers:** `もし`, `ても`, `でも`
- **Token Formation Patterns:**
  - `もし` + [verb] + `も` + `もし` + [adjective] + `ても` + `もし` + [adjective] + [noun] + `でも`

### 必ずしも～とは限らない (kanarazushimo ～ towa kagiranai)
**Original Formation String:** `必ずしも + Statement + とは限らない`
- **String Markers:** `必ずしも`, `とは限らない`
- **Token Formation Patterns:** *None successfully parsed*

### 決して～ない (kesshite ~ nai)
**Original Formation String:** `決して + Verb (negative form)`
- **String Markers:** `決して`
- **Token Formation Patterns:**
  - `決して` + [verb]

### ～うちに (〜uchi ni)
**Original Formation String:** `Verb-てform + いる + うちに, い-Adjective + い + うちに, な-Adjective + な + うちに`
- **String Markers:** `うちに`
- **Token Formation Patterns:**
  - [verb] + `いる` + `うちに`
  - [adjective] + `い` + `うちに`
  - [adjective] + `な` + `うちに`

### ～うとした (〜uto shita)
**Original Formation String:** `Verb-う stem + とした`
- **String Markers:** `うとした`, `とした`
- **Token Formation Patterns:**
  - [verb] + `とした`

### ～おかげで (〜okagede)
**Original Formation String:** `Verb-casual + おかげで, い-Adjective + おかげで, な-Adjective + だおかげで, Noun + のおかげで`
- **String Markers:** `おかげで`, `だおかげで`, `のおかげで`
- **Token Formation Patterns:**
  - [verb] + `おかげで`
  - [adjective] + `おかげで`
  - [adjective] + `だおかげで`
  - [noun] + `のおかげで`

### ～かけ (〜kake)
**Original Formation String:** `Verb-ますstem + かけ`
- **String Markers:** `かけ`
- **Token Formation Patterns:**
  - [verb] + `かけ`

### ～かなあ (〜kanaa)
**Original Formation String:** `Verb-casual + かなあ, い-Adjective + かなあ, な-Adjective + だかなあ, Noun + だかなあ`
- **String Markers:** `かなあ`, `だかなあ`
- **Token Formation Patterns:**
  - [verb] + `かなあ`
  - [adjective] + `かなあ`
  - [adjective] + `だかなあ`
  - [noun] + `だかなあ`

### ～から～にかけて (〜kara 〜ni kakete)
**Original Formation String:** `Noun (time, place, or measure) + から + Noun (time, place or measure) + にかけて`
- **String Markers:** `から`, `にかけて`
- **Token Formation Patterns:**
  - [noun] + `から` + [noun] + `にかけて`

### ～かわりに (〜kawari ni)
**Original Formation String:** `Verb-casual + かわりに, い-Adjective + かわりに, な-Adjective + だかわりに, Noun + だかわりに`
- **String Markers:** `かわりに`, `だかわりに`
- **Token Formation Patterns:**
  - [verb] + `かわりに`
  - [adjective] + `かわりに`
  - [adjective] + `だかわりに`
  - [noun] + `だかわりに`

### ～きり (〜kiri)
**Original Formation String:** `Verb-past + きり, Verb-てform + きり (less common), Noun + きり`
- **String Markers:** `きり`
- **Token Formation Patterns:**
  - [verb] + `きり`
  - [verb] + `きり`
  - [noun] + `きり`

### ～くせに (〜kuse ni)
**Original Formation String:** `Verb-casual + くせに, い-Adjective + くせに, な-Adjective + な/のくせに, Noun + のくせに`
- **String Markers:** `くせに`, `のくせに`
- **Token Formation Patterns:**
  - [verb] + `くせに`
  - [adjective] + `くせに`
  - [adjective] + `な` + `のくせに`
  - [noun] + `のくせに`

### ～くらい (〜kurai)
**Original Formation String:** `Verb-casual + くらい, い-Adjective + くらい, な-Adjective + くらい, Noun + くらい`
- **String Markers:** `くらい`
- **Token Formation Patterns:**
  - [verb] + `くらい`
  - [adjective] + `くらい`
  - [adjective] + `くらい`
  - [noun] + `くらい`

### ～くらい～は～ない (〜kurai 〜wa 〜nai)
**Original Formation String:** `Verb-casual (non-past) + くらい + は + Verb-casual (negative), Adjective (non-past) + くらい + は + Adjective (negative)`
- **String Markers:** `くらい`
- **Token Formation Patterns:**
  - [verb] + `くらい` + `は` + [verb]
  - [adjective] + `くらい` + `は` + [adjective]

### ～こそ (〜koso)
**Original Formation String:** `Noun + こそ, (Verb-て + こそ)`
- **String Markers:** `こそ`
- **Token Formation Patterns:**
  - [noun] + `こそ` + [verb] + `こそ`

### ～こと (〜koto)
**Original Formation String:** `Verb-plain form + こと, Verb-phrase in plain form + こと`
- **String Markers:** `こと`
- **Token Formation Patterns:**
  - [verb] + `こと`
  - [verb] + `こと`

### ～ことだ (〜koto da)
**Original Formation String:** `Verb-ますstem + ことだ, い-Adjective + ことだ, な-Adjective + なことだ, Noun + のことだ`
- **String Markers:** `ことだ`, `なことだ`, `のことだ`
- **Token Formation Patterns:**
  - [verb] + `ことだ`
  - [adjective] + `ことだ`
  - [adjective] + `なことだ`
  - [noun] + `のことだ`

### ～ことにしている (〜koto ni shite iru)
**Original Formation String:** `Verb-casual + ことにしている`
- **String Markers:** `ことにしている`
- **Token Formation Patterns:**
  - [verb] + `ことにしている`

### ～ことになっている (〜koto ni natte iru)
**Original Formation String:** `Verb-dictionary form + ことになっている`
- **String Markers:** `ことになっている`
- **Token Formation Patterns:**
  - [verb] + `ことになっている`

### ～ことは…が (～koto wa... ga)
**Original Formation String:** `Verb-casual + ことは + が, い-Adjective + ことは + が, な-Adjective + だ + ことは + が, Noun + だ + ことは + が`
- **String Markers:** `ことは`
- **Token Formation Patterns:**
  - [verb] + `ことは` + `が`
  - [adjective] + `ことは` + `が`
  - [adjective] + `だ` + `ことは` + `が`
  - [noun] + `だ` + `ことは` + `が`

### ～ことはない (〜koto wa nai)
**Original Formation String:** `Verb-dictionary form + ことはない, い-Adjective + ことはない, な-Adjective + であることはない, Noun + であることはない`
- **String Markers:** `ことはない`, `であることはない`
- **Token Formation Patterns:**
  - [verb] + `ことはない`
  - [adjective] + `ことはない`
  - [adjective] + `であることはない`
  - [noun] + `であることはない`

### ～さえ (～sae)
**Original Formation String:** `Noun + さえ, Verb-casual + さえ, い-Adjective + さえ, な-Adjective + でさえ`
- **String Markers:** `さえ`, `でさえ`
- **Token Formation Patterns:**
  - [noun] + `さえ`
  - [verb] + `さえ`
  - [adjective] + `さえ`
  - [adjective] + `でさえ`

### ～しかない (〜shika nai)
**Original Formation String:** `Verb-casual + しかない, い-Adjective + しかない, な-Adjective + しかない, Noun + しかない`
- **String Markers:** `しかない`
- **Token Formation Patterns:**
  - [verb] + `しかない`
  - [adjective] + `しかない`
  - [adjective] + `しかない`
  - [noun] + `しかない`

### ～ずに (〜zu ni)
**Original Formation String:** `Verb-ない form (Remove ない) + ずに`
- **String Markers:** `ずに`
- **Token Formation Patterns:**
  - [verb] + `ずに`

### ～せいで (〜sei de)
**Original Formation String:** `Verb-casual + せいで, い-Adjective + せいで, な-Adjective + なせいで, Noun + のせいで`
- **String Markers:** `せいで`, `なせいで`, `のせいで`
- **Token Formation Patterns:**
  - [verb] + `せいで`
  - [adjective] + `せいで`
  - [adjective] + `なせいで`
  - [noun] + `のせいで`

### ～せてください (〜sete kudasai)
**Original Formation String:** `Verb-causative (させ) + て + ください`
- **String Markers:** `せてください`, `させ`, `ください`
- **Token Formation Patterns:**
  - [verb] + `て` + `ください`

### ～そのために (〜sono tame ni)
**Original Formation String:** `Sentence/phrase 1 + そのために + Sentence/phrase 2`
- **String Markers:** `そのために`
- **Token Formation Patterns:** *None successfully parsed*

### ～その結果 (〜sono kekka)
**Original Formation String:** `Situation/ACTION 1 + その結果 + RESULT`
- **String Markers:** `その結果`
- **Token Formation Patterns:** *None successfully parsed*

### ～それと～ (〜sore to〜)
**Original Formation String:** `Item1 + それと + Item2`
- **String Markers:** `それと`
- **Token Formation Patterns:** *None successfully parsed*

### ～たて (～tate)
**Original Formation String:** `Verb-stem + たて`
- **String Markers:** `たて`
- **Token Formation Patterns:**
  - [verb] + `たて`

### ～たとえ～ても (〜tatoe〜temo)
**Original Formation String:** `たとえ + Verb-casual + ても, たとえ + い-Adjective + くても, たとえ + な-Adjective + であっても, たとえ + Noun + であっても`
- **String Markers:** `たとえ`, `ても`, `くても`, `であっても`
- **Token Formation Patterns:**
  - `たとえ` + [verb] + `ても` + `たとえ` + [adjective] + `くても` + `たとえ` + [adjective] + `であっても` + `たとえ` + [noun] + `であっても`

### ～たところ (〜ta tokoro)
**Original Formation String:** `Verb-た form + ところ`
- **String Markers:** `たところ`, `ところ`
- **Token Formation Patterns:**
  - [verb] + `ところ`

### ～たとたん (〜ta totan)
**Original Formation String:** `Verb-た form + とたん`
- **String Markers:** `たとたん`, `とたん`
- **Token Formation Patterns:**
  - [verb] + `とたん`

### ～たびに (〜tabi ni)
**Original Formation String:** `Verb-dictionary form + たびに, Noun + のたびに`
- **String Markers:** `たびに`, `のたびに`
- **Token Formation Patterns:**
  - [verb] + `たびに`
  - [noun] + `のたびに`

### ～だけしか (～dake shika)
**Original Formation String:** `Noun/Quantity + だけ + しか + Negative Verb`
- **String Markers:** `だけしか`, `だけ`, `しか`
- **Token Formation Patterns:**
  - [noun] + `だけ` + `しか` + [verb]

### ～だものだ (〜da mono da)
**Original Formation String:** `Verb-casual + んだものだ, い-Adjective + んだものだ, な-Adjective + なんだものだ, Noun + なんだものだ (often with から as んだものだから)`
- **String Markers:** `だものだ`, `んだものだ`, `なんだものだ`, `から`
- **Token Formation Patterns:**
  - [verb] + `んだものだ`
  - [adjective] + `んだものだ`
  - [adjective] + `なんだものだ`
  - [noun] + `なんだものだ`

### ～ちゃった (〜chatta)
**Original Formation String:** `Verb-て/で form → ちゃった/じゃった (e.g. 食べてしまった → 食べちゃった)`
- **String Markers:** `ちゃった`, `じゃった`, `食べてしまった`, `食べちゃった`
- **Token Formation Patterns:**
  - [verb] + `で` + `ちゃった` + `じゃった`

### ～っけ？ (〜kke?)
**Original Formation String:** `Verb-casual + っけ?, い-Adjective + かったっけ?, な-Adjective/Noun + だっけ?`
- **String Markers:** `っけ`, `かったっけ`, `だっけ`
- **Token Formation Patterns:**
  - [verb] + `っけ`
  - [adjective] + `かったっけ`
  - [adjective] + [noun] + `だっけ`

### ～っぱい (〜ppai)
**Original Formation String:** `Noun + で + いっぱい (Note: written as いっぱい, read as 'ippai')`
- **String Markers:** `っぱい`, `いっぱい`
- **Token Formation Patterns:**
  - [noun] + `で` + `いっぱい`

### ～っぱなし (〜ppanashi)
**Original Formation String:** `Verb-ますstem + っぱなし`
- **String Markers:** `っぱなし`
- **Token Formation Patterns:**
  - [verb] + `っぱなし`

### ～ついでに (〜tsuide ni)
**Original Formation String:** `Verb (dictionary or た-form) + ついでに, Noun + の + ついでに, or Verb-て form + いる + ついでに`
- **String Markers:** `ついでに`
- **Token Formation Patterns:**
  - [verb] + `ついでに`
  - [noun] + `の` + `ついでに` + [verb] + `いる` + `ついでに`

### ～つまり (〜tsumari)
**Original Formation String:** `Sentence A + つまり + Sentence B (rephrasing)`
- **String Markers:** `つまり`
- **Token Formation Patterns:** *None successfully parsed*

### ～つもりでした (〜tsumori deshita)
**Original Formation String:** `Verb-casual (dictionary form) + つもりでした`
- **String Markers:** `つもりでした`
- **Token Formation Patterns:**
  - [verb] + `つもりでした`

### ～ている (〜te iru)
**Original Formation String:** `Verb-て form + いる`
- **String Markers:** `ている`
- **Token Formation Patterns:**
  - [verb] + `いる`

### ～てくれと (〜te kureto)
**Original Formation String:** `Verb-て form + くれと (言う / 頼む / 伝える, etc.)`
- **String Markers:** `てくれと`, `くれと言う`, `頼む`, `伝える`
- **Token Formation Patterns:**
  - [verb] + `くれと`

### ～てごらん (〜te goran)
**Original Formation String:** `Verb-て form + ごらん`
- **String Markers:** `てごらん`, `ごらん`
- **Token Formation Patterns:**
  - [verb] + `ごらん`

### ～てはじめて (〜te hajimete)
**Original Formation String:** `Verb-て form + はじめて`
- **String Markers:** `てはじめて`, `はじめて`
- **Token Formation Patterns:**
  - [verb] + `はじめて`

### ～てほしい (〜te hoshii)
**Original Formation String:** `Verb-て form + ほしい`
- **String Markers:** `てほしい`, `ほしい`
- **Token Formation Patterns:**
  - [verb] + `ほしい`

### ～てみる (〜te miru)
**Original Formation String:** `Verb-て form + みる`
- **String Markers:** `てみる`, `みる`
- **Token Formation Patterns:**
  - [verb] + `みる`

### ～ても (〜temo)
**Original Formation String:** `Verb-て form + も, い-Adjective (～く) + ても, な-Adjective/Noun (～で) + も`
- **String Markers:** `ても`
- **Token Formation Patterns:**
  - [verb] + `も`
  - [adjective] + `ても`
  - [adjective] + [noun] + `も`

### ～といいなあ (〜to ii naa)
**Original Formation String:** `Verb-casual + といいなあ, い-Adjective + といいなあ, な-Adjective + だといいなあ, Noun + だといいなあ`
- **String Markers:** `といいなあ`, `だといいなあ`
- **Token Formation Patterns:**
  - [verb] + `といいなあ`
  - [adjective] + `といいなあ`
  - [adjective] + `だといいなあ`
  - [noun] + `だといいなあ`

### ～という (〜to iu)
**Original Formation String:** `Noun + という + Noun, Verb-casual + という + Noun, い-Adjective + という + Noun, な-Adjective + という + Noun`
- **String Markers:** `という`
- **Token Formation Patterns:**
  - [noun] + `という` + [noun]
  - [verb] + `という` + [noun]
  - [adjective] + `という` + [noun]
  - [adjective] + `という` + [noun]

### ～ということだ (〜to iu koto da)
**Original Formation String:** `Verb-casual + ということだ, い-Adjective + ということだ, な-Adjective + だということだ, Noun + だということだ`
- **String Markers:** `ということだ`, `だということだ`
- **Token Formation Patterns:**
  - [verb] + `ということだ`
  - [adjective] + `ということだ`
  - [adjective] + `だということだ`
  - [noun] + `だということだ`

### ～というと (〜to iu to)
**Original Formation String:** `Noun + というと`
- **String Markers:** `というと`
- **Token Formation Patterns:**
  - [noun] + `というと`

### ～というのは (〜to iu no wa)
**Original Formation String:** `Phrase/sentence + というのは + explanation/definition`
- **String Markers:** `というのは`
- **Token Formation Patterns:** *None successfully parsed*

### ～というの～ (〜to iu no〜)
**Original Formation String:** `Verb-casual + というの, い-Adjective + というの, な-Adjective + だというの, Noun + だというの`
- **String Markers:** `というの`, `だというの`
- **Token Formation Patterns:**
  - [verb] + `というの`
  - [adjective] + `というの`
  - [adjective] + `だというの`
  - [noun] + `だというの`

### ～というより (〜to iu yori)
**Original Formation String:** `Verb-casual + というより, い-Adjective + というより, な-Adjective + だというより, Noun + だというより`
- **String Markers:** `というより`, `だというより`
- **Token Formation Patterns:**
  - [verb] + `というより`
  - [adjective] + `というより`
  - [adjective] + `だというより`
  - [noun] + `だというより`

### ～といっても (〜to ittemo)
**Original Formation String:** `Verb-casual + といっても, い-Adjective + といっても, な-Adjective + だといっても, Noun + だといっても`
- **String Markers:** `といっても`, `だといっても`
- **Token Formation Patterns:**
  - [verb] + `といっても`
  - [adjective] + `といっても`
  - [adjective] + `だといっても`
  - [noun] + `だといっても`

### ～とおり (〜toori)
**Original Formation String:** `Verb-て form + とおり, Noun + のとおり`
- **String Markers:** `とおり`, `のとおり`
- **Token Formation Patterns:**
  - [verb] + `とおり`
  - [noun] + `のとおり`

### ～とく (〜toku)
**Original Formation String:** `Verb-て form + とく (e.g., 食べておく→食べとく, 読んでおく→読んどく)`
- **String Markers:** `とく`, `食べておく`, `食べとく`, `読んでおく`
- **Token Formation Patterns:**
  - [verb] + `とく`

### ～ところが (〜tokoro ga)
**Original Formation String:** `Phrase 1 (expected situation) + ところが + Phrase 2 (unexpected result)`
- **String Markers:** `ところが`
- **Token Formation Patterns:** *None successfully parsed*

### ～ところだった (〜tokoro datta)
**Original Formation String:** `Verb (dictionary form or ている form) + ところだった`
- **String Markers:** `ところだった`, `ている`
- **Token Formation Patterns:**
  - [verb] + `ところだった`

### ～としたら (〜to shitara)
**Original Formation String:** `Verb-casual + としたら, い-Adjective + としたら, な-Adjective + だとしたら, Noun + だとしたら`
- **String Markers:** `としたら`, `だとしたら`
- **Token Formation Patterns:**
  - [verb] + `としたら`
  - [adjective] + `としたら`
  - [adjective] + `だとしたら`
  - [noun] + `だとしたら`

### ～として (〜to shite)
**Original Formation String:** `Verb-casual + として, い-Adjective + として, な-Adjective + だとして, Noun + だとして`
- **String Markers:** `として`, `だとして`
- **Token Formation Patterns:**
  - [verb] + `として`
  - [adjective] + `として`
  - [adjective] + `だとして`
  - [noun] + `だとして`

### ～どんなに～ことか (〜donna ni〜koto ka)
**Original Formation String:** `どんなに + Adjective + ことか, どんなに + Verb + ことか`
- **String Markers:** `どんなに`, `ことか`
- **Token Formation Patterns:**
  - `どんなに` + [adjective] + `ことか` + `どんなに` + [verb] + `ことか`

### ～ないことはない (〜nai koto wa nai)
**Original Formation String:** `Verb-ない form + ことはない`
- **String Markers:** `ないことはない`, `ことはない`
- **Token Formation Patterns:**
  - [verb] + `ことはない`

### ～ないで (〜naide)
**Original Formation String:** `Verb-ない-form + で`
- **String Markers:** `ないで`
- **Token Formation Patterns:**
  - [verb] + `で`

### ～ないと (〜nai to)
**Original Formation String:** `Verb-negative form + ないと`
- **String Markers:** `ないと`
- **Token Formation Patterns:**
  - [verb] + `ないと`

### ～なぜなら (〜nazenara)
**Original Formation String:** `Sentence/Statement + なぜなら + Reason + から/だから`
- **String Markers:** `なぜなら`, `から`, `だから`
- **Token Formation Patterns:** *None successfully parsed*

### ～など (〜nado)
**Original Formation String:** `Noun + など`
- **String Markers:** `など`
- **Token Formation Patterns:**
  - [noun] + `など`

### ～なんか (〜nanka)
**Original Formation String:** `Noun + なんか, Verb-casual + なんか, い-Adjective + なんか, な-Adjective + なんか`
- **String Markers:** `なんか`
- **Token Formation Patterns:**
  - [noun] + `なんか`
  - [verb] + `なんか`
  - [adjective] + `なんか`
  - [adjective] + `なんか`

### ～において (〜ni oite)
**Original Formation String:** `Noun (Place/Time/Context) + において`
- **String Markers:** `において`
- **Token Formation Patterns:**
  - [noun] + `において`

### ～にかわって (〜ni kawatte)
**Original Formation String:** `Noun + にかわって`
- **String Markers:** `にかわって`
- **Token Formation Patterns:**
  - [noun] + `にかわって`

### ～にしては (〜ni shite wa)
**Original Formation String:** `Verb-casual + にしては, い-Adjective + にしては, な-Adjective + にしては, Noun + にしては`
- **String Markers:** `にしては`
- **Token Formation Patterns:**
  - [verb] + `にしては`
  - [adjective] + `にしては`
  - [adjective] + `にしては`
  - [noun] + `にしては`

### ～にしても (〜ni shitemo)
**Original Formation String:** `Verb-casual + にしても, い-Adjective + にしても, な-Adjective + だにしても, Noun + だにしても`
- **String Markers:** `にしても`, `だにしても`
- **Token Formation Patterns:**
  - [verb] + `にしても`
  - [adjective] + `にしても`
  - [adjective] + `だにしても`
  - [noun] + `だにしても`

### ～について (〜ni tsuite)
**Original Formation String:** `Noun + について`
- **String Markers:** `について`
- **Token Formation Patterns:**
  - [noun] + `について`

### ～にとって (〜ni totte)
**Original Formation String:** `Noun (person or thing) + にとって + Verb/Adjective/Noun`
- **String Markers:** `にとって`
- **Token Formation Patterns:**
  - [noun] + `にとって` + [verb] + [adjective] + [noun]

### ～によって (〜ni yotte)
**Original Formation String:** `Verb-casual + によって, い-Adjective + によって, な-Adjective + によって, Noun + によって`
- **String Markers:** `によって`
- **Token Formation Patterns:**
  - [verb] + `によって`
  - [adjective] + `によって`
  - [adjective] + `によって`
  - [noun] + `によって`

### ～によれば (〜ni yoreba)
**Original Formation String:** `Noun + によれば`
- **String Markers:** `によれば`
- **Token Formation Patterns:**
  - [noun] + `によれば`

### ～に対して (～ni taishite)
**Original Formation String:** `Verb-casual + に対して, い-Adjective + に対して, な-Adjective + に対して, Noun + に対して`
- **String Markers:** `に対して`
- **Token Formation Patterns:**
  - [verb] + `に対して`
  - [adjective] + `に対して`
  - [adjective] + `に対して`
  - [noun] + `に対して`

### ～に比べて (〜ni kurabete)
**Original Formation String:** `Verb-casual + に比べて, い-Adjective + に比べて, な-Adjective + だ/である + に比べて, Noun + だ/である + に比べて`
- **String Markers:** `に比べて`, `である`
- **Token Formation Patterns:**
  - [verb] + `に比べて`
  - [adjective] + `に比べて`
  - [adjective] + `だ` + `である` + `に比べて`
  - [noun] + `だ` + `である` + `に比べて`

### ～に関して (〜ni kanshite)
**Original Formation String:** `Noun + に関して`
- **String Markers:** `に関して`
- **Token Formation Patterns:**
  - [noun] + `に関して`

### ～はずだ (〜hazu da)
**Original Formation String:** `Verb-casual + はずだ, い-Adjective + はずだ, な-Adjective + なはずだ, Noun + のはずだ`
- **String Markers:** `はずだ`, `なはずだ`, `のはずだ`
- **Token Formation Patterns:**
  - [verb] + `はずだ`
  - [adjective] + `はずだ`
  - [adjective] + `なはずだ`
  - [noun] + `のはずだ`

### ～はもちろん～も (〜wa mochiron 〜mo)
**Original Formation String:** `Noun1 + はもちろん + Noun2 + も`
- **String Markers:** `はもちろん`
- **Token Formation Patterns:**
  - [noun] + `はもちろん` + [noun] + `も`

### ～ばかり (〜bakari)
**Original Formation String:** `Verb-ますstem + ばかり, い-Adjective + ばかり, な-Adjective + ばかり, Noun + ばかり`
- **String Markers:** `ばかり`
- **Token Formation Patterns:**
  - [verb] + `ばかり`
  - [adjective] + `ばかり`
  - [adjective] + `ばかり`
  - [noun] + `ばかり`

### ～ばかりか (〜bakarika) ～も (mo)
**Original Formation String:** `Verb-casual + ばかりか/も, い-Adjective + ばかりか/も, な-Adjective + だ + ばかりか/も, Noun + だ + ばかりか/も`
- **String Markers:** `ばかりか`
- **Token Formation Patterns:**
  - [verb] + `ばかりか` + `も`
  - [adjective] + `ばかりか` + `も`
  - [adjective] + `だ` + `ばかりか` + `も`
  - [noun] + `だ` + `ばかりか` + `も`

### ～ばよかった (〜ba yokatta)
**Original Formation String:** `Verb-ば-form + よかった, い-Adjective-く + ばよかった, な-Adjective + ならよかった`
- **String Markers:** `ばよかった`, `よかった`, `ならよかった`
- **Token Formation Patterns:**
  - [verb] + `よかった`
  - [adjective] + `く` + `ばよかった`
  - [adjective] + `ならよかった`

### ～ば～のに (〜ba 〜noni)
**Original Formation String:** `Verb-ば form + ～のに, い-Adjective-ば form + ～のに, な-Adjective + であれば + ～のに, Noun + であれば + ～のに`
- **String Markers:** `のに`, `であれば`
- **Token Formation Patterns:**
  - [verb] + `のに`
  - [adjective] + `ば` + `のに`
  - [adjective] + `であれば` + `のに`
  - [noun] + `であれば` + `のに`

### ～ば～ほど (〜ba 〜hodo)
**Original Formation String:** `Verb-casual + ば + Verb-casual + ほど, い-Adjective + ば + い-Adjective + ほど, な-Adjective + であれば + な-Adjective + ほど`
- **String Markers:** `ほど`, `であれば`
- **Token Formation Patterns:**
  - [verb] + `ば` + [verb] + `ほど`
  - [adjective] + `ば` + [adjective] + `ほど`
  - [adjective] + `であれば` + [adjective] + `ほど`

### ～ふりをする (〜furi wo suru)
**Original Formation String:** `Verb (dictionary form) + ふりをする, い-Adjective + ふりをする, な-Adjective + ふりをする, Noun + ふりをする`
- **String Markers:** `ふりをする`
- **Token Formation Patterns:**
  - [verb] + `ふりをする`
  - [adjective] + `ふりをする`
  - [adjective] + `ふりをする`
  - [noun] + `ふりをする`

### ～べきだ (〜beki da)
**Original Formation String:** `Verb-dictionary form + べきだ`
- **String Markers:** `べきだ`
- **Token Formation Patterns:**
  - [verb] + `べきだ`

### ～ほど～ (〜hodo〜)
**Original Formation String:** `Verb-casual + ほど, い-Adjective + ほど, な-Adjective + ほど, Noun + ほど`
- **String Markers:** `ほど`
- **Token Formation Patterns:**
  - [verb] + `ほど`
  - [adjective] + `ほど`
  - [adjective] + `ほど`
  - [noun] + `ほど`

### ～ますように (〜masu you ni)
**Original Formation String:** `Verb-ます form, remove final る + ように`
- **String Markers:** `ますように`, `ように`
- **Token Formation Patterns:**
  - [verb] + `る` + `ように`

### ～まで (〜made)
**Original Formation String:** `Verb-casual + まで, い-Adjective + まで, な-Adjective + まで, Noun + まで`
- **String Markers:** `まで`
- **Token Formation Patterns:**
  - [verb] + `まで`
  - [adjective] + `まで`
  - [adjective] + `まで`
  - [noun] + `まで`

### ～まま (〜mama)
**Original Formation String:** `Verb-ます stem + まま, い-Adjective + まま, な-Adjective + なまま, Noun + のまま`
- **String Markers:** `まま`, `なまま`, `のまま`
- **Token Formation Patterns:**
  - [verb] + `まま`
  - [adjective] + `まま`
  - [adjective] + `なまま`
  - [noun] + `のまま`

### ～みたいだ (〜mitai da)
**Original Formation String:** `Verb-casual + みたいだ, い-Adjective + みたいだ, な-Adjective + みたいだ, Noun + みたいだ`
- **String Markers:** `みたいだ`
- **Token Formation Patterns:**
  - [verb] + `みたいだ`
  - [adjective] + `みたいだ`
  - [adjective] + `みたいだ`
  - [noun] + `みたいだ`

### ～めったにない (〜metta ni nai)
**Original Formation String:** `Verb-negative + めったにない, い-Adjective-negative + めったにない, な-Adjective-negative + めったにない, Noun-negative + めったにない`
- **String Markers:** `めったにない`
- **Token Formation Patterns:**
  - [verb] + `めったにない`
  - [adjective] + `めったにない`
  - [adjective] + `めったにない`
  - [noun] + `めったにない`

### ～めったに～ない (〜metta ni 〜nai)
**Original Formation String:** `めったに + Verb[ない-form] / めったに + い-Adjective[ない-form] / めったに + な-Adjective[じゃない/ではない-form]`
- **String Markers:** `めったに`, `じゃない`, `ではない`
- **Token Formation Patterns:**
  - `めったに` + [verb] + `めったに` + [adjective] + `めったに` + [adjective]

### ～ようとしない (〜you to shinai)
**Original Formation String:** `Verb-volitional form + としない`
- **String Markers:** `ようとしない`, `としない`
- **Token Formation Patterns:**
  - [verb] + `としない`

### ～ようと思う (〜you to omou)
**Original Formation String:** `Verb-volitional + と思う`
- **String Markers:** `ようと思う`, `と思う`
- **Token Formation Patterns:**
  - [verb] + `と思う`

### ～ように (〜you ni)
**Original Formation String:** `Verb-casual + ように, い-Adjective + ように, な-Adjective + に, Noun + のように`
- **String Markers:** `ように`, `のように`
- **Token Formation Patterns:**
  - [verb] + `ように`
  - [adjective] + `ように`
  - [adjective] + `に`
  - [noun] + `のように`

### ～ように (〜you ni)
**Original Formation String:** `Verb-casual + ように, い-Adjective + ように, な-Adjective + だように, Noun + のように`
- **String Markers:** `ように`, `だように`, `のように`
- **Token Formation Patterns:**
  - [verb] + `ように`
  - [adjective] + `ように`
  - [adjective] + `だように`
  - [noun] + `のように`

### ～ように (〜you ni)
**Original Formation String:** `Verb-casual + ように, い-Adjective + ように, な-Adjective + に, Noun + のように`
- **String Markers:** `ように`, `のように`
- **Token Formation Patterns:**
  - [verb] + `ように`
  - [adjective] + `ように`
  - [adjective] + `に`
  - [noun] + `のように`

### ～ようにしましょう (〜you ni shimashou)
**Original Formation String:** `Verb-dictionary form + ようにしましょう / Verb-negative form + ようにしましょう`
- **String Markers:** `ようにしましょう`
- **Token Formation Patterns:**
  - [verb] + `ようにしましょう` + [verb] + `ようにしましょう`

### ～ようになった (〜you ni natta)
**Original Formation String:** `Verb-casual + ようになった`
- **String Markers:** `ようになった`
- **Token Formation Patterns:**
  - [verb] + `ようになった`

### ～ように言う (〜you ni iu)
**Original Formation String:** `Verb-dictionary form + ように言う / Verb-nai form + ように言う`
- **String Markers:** `ように言う`
- **Token Formation Patterns:**
  - [verb] + `ように言う` + [verb] + `ように言う`

### ～らしい (〜rashii)
**Original Formation String:** `Verb-casual + らしい, い-Adjective + らしい, な-Adjective + だらしい, Noun + だらしい`
- **String Markers:** `らしい`, `だらしい`
- **Token Formation Patterns:**
  - [verb] + `らしい`
  - [adjective] + `らしい`
  - [adjective] + `だらしい`
  - [noun] + `だらしい`

### ～られた (〜rareta)
**Original Formation String:** `Verb (passive form, past tense) + られた`
- **String Markers:** `られた`
- **Token Formation Patterns:**
  - [verb] + `られた`

### ～わけがない (〜wake ga nai)
**Original Formation String:** `Verb-casual + わけがない, い-Adjective + わけがない, な-Adjective + なわけがない, Noun + のわけがない`
- **String Markers:** `わけがない`, `なわけがない`, `のわけがない`
- **Token Formation Patterns:**
  - [verb] + `わけがない`
  - [adjective] + `わけがない`
  - [adjective] + `なわけがない`
  - [noun] + `のわけがない`

### ～わけだ (〜wake da)
**Original Formation String:** `Verb-casual + わけだ, い-Adjective + わけだ, な-Adjective + なわけだ, Noun + のわけだ`
- **String Markers:** `わけだ`, `なわけだ`, `のわけだ`
- **Token Formation Patterns:**
  - [verb] + `わけだ`
  - [adjective] + `わけだ`
  - [adjective] + `なわけだ`
  - [noun] + `のわけだ`

### ～わけではない (〜wake dewa nai)
**Original Formation String:** `Verb-casual + わけではない, い-Adjective + わけではない, な-Adjective + だわけではない, Noun + だわけではない`
- **String Markers:** `わけではない`, `だわけではない`
- **Token Formation Patterns:**
  - [verb] + `わけではない`
  - [adjective] + `わけではない`
  - [adjective] + `だわけではない`
  - [noun] + `だわけではない`

### ～わけにはいかない (〜wake ni wa ikanai)
**Original Formation String:** `Verb-casual + わけにはいかない`
- **String Markers:** `わけにはいかない`
- **Token Formation Patterns:**
  - [verb] + `わけにはいかない`

### ～わりには (〜wari ni wa)
**Original Formation String:** `Verb-casual + わりには, い-Adjective + わりには, な-Adjective + だわりには, Noun + だわりには`
- **String Markers:** `わりには`, `だわりには`
- **Token Formation Patterns:**
  - [verb] + `わりには`
  - [adjective] + `わりには`
  - [adjective] + `だわりには`
  - [noun] + `だわりには`

### ～んだって (〜n datte)
**Original Formation String:** `Verb-casual + んだって, い-Adjective + んだって, な-Adjective + なんだって, Noun + なんだって`
- **String Markers:** `んだって`, `なんだって`
- **Token Formation Patterns:**
  - [verb] + `んだって`
  - [adjective] + `んだって`
  - [adjective] + `なんだって`
  - [noun] + `なんだって`

### ～んだもん (〜nda mon)
**Original Formation String:** `Verb-casual + んだもん, い-Adjective + んだもん, な-Adjective + なんだもん, Noun + なんだもん`
- **String Markers:** `んだもん`, `なんだもん`
- **Token Formation Patterns:**
  - [verb] + `んだもん`
  - [adjective] + `んだもん`
  - [adjective] + `なんだもん`
  - [noun] + `なんだもん`

### ～上げる (〜ageru)
**Original Formation String:** `Verb-ますstem + 上げる`
- **String Markers:** `上げる`
- **Token Formation Patterns:**
  - [verb] + `上げる`

### ～切れない (～kirenai)
**Original Formation String:** `Verb-stem + 切れない`
- **String Markers:** `切れない`
- **Token Formation Patterns:**
  - [verb] + `切れない`

### ～最中に (～saichuu ni)
**Original Formation String:** `Verb-て form + いる + 最中に, Noun + の + 最中に`
- **String Markers:** `最中に`
- **Token Formation Patterns:**
  - [verb] + `いる` + `最中に`
  - [noun] + `の` + `最中に`

### ～？それとも～？ (～? sore tomo ～?)
**Original Formation String:** `Verb-casual + ？それとも + Verb-casual + ？, etc.`
- **String Markers:** `それとも`
- **Token Formation Patterns:**
  - [verb] + `それとも` + [verb]

## N2

### A あるいは B (A aruiwa B)
**Original Formation String:** `Phrase A + あるいは + Phrase B`
- **String Markers:** `あるいは`
- **Token Formation Patterns:** *None successfully parsed*

### A すなわち B。 (A sunawachi B)
**Original Formation String:** `Phrase A + すなわち + Phrase B`
- **String Markers:** `すなわち`
- **Token Formation Patterns:** *None successfully parsed*

### A それはそうと B。 (A Sore wa sou to B)
**Original Formation String:** `Sentence A + それはそうと + Sentence B`
- **String Markers:** `それはそうと`
- **Token Formation Patterns:** *None successfully parsed*

### A。おまけに B。(~omake ni)
**Original Formation String:** `Sentence A + おまけに  + Sentence B`
- **String Markers:** `おまけに`
- **Token Formation Patterns:** *None successfully parsed*

### A。さて B。(A. Sate B.)
**Original Formation String:** `A + さて + B`
- **String Markers:** `さて`
- **Token Formation Patterns:** *None successfully parsed*

### A。しかも B。(A. Shikamo B.)
**Original Formation String:** `Statement A + 。しかも + Statement B。`
- **String Markers:** `しかも`
- **Token Formation Patterns:** *None successfully parsed*

### A。したがって B。(A. Shitagatte B.)
**Original Formation String:** `A + したがって + B`
- **String Markers:** `したがって`
- **Token Formation Patterns:** *None successfully parsed*

### A。すると B。(~suruto)
**Original Formation String:** `A (Sentence) + すると + B (Sentence)`
- **String Markers:** `すると`
- **Token Formation Patterns:** *None successfully parsed*

### A。そういえば B。(~souieba)
**Original Formation String:** `A + そういえば + B`
- **String Markers:** `そういえば`
- **Token Formation Patterns:** *None successfully parsed*

### A。そこで B。(~sokode)
**Original Formation String:** `A + そこで + B`
- **String Markers:** `そこで`
- **Token Formation Patterns:** *None successfully parsed*

### A。それがB。(~sorega)
**Original Formation String:** `A (Statement)。それが B (Restatement or explanation of A)。`
- **String Markers:** `それが`
- **Token Formation Patterns:** *None successfully parsed*

### A。それで B。 (~sore de)
**Original Formation String:** `Sentence A +。それで+ Sentence B。`
- **String Markers:** `それで`
- **Token Formation Patterns:** *None successfully parsed*

### A。それでも B。(~sore demo)
**Original Formation String:** `A (situation) + 。それでも + B (action or thought)`
- **String Markers:** `それでも`
- **Token Formation Patterns:** *None successfully parsed*

### A。それなのに B。(~sorenanoni)
**Original Formation String:** `A。それなのに B。`
- **String Markers:** `それなのに`
- **Token Formation Patterns:** *None successfully parsed*

### A。それなら B。(A. Sore nara B.)
**Original Formation String:** `Situation A (sentence) + 。それなら + Situation B (sentence)`
- **String Markers:** `それなら`
- **Token Formation Patterns:** *None successfully parsed*

### A。ただB。(~tada)
**Original Formation String:** `Sentence A + ただ + Sentence B`
- **String Markers:** `ただ`
- **Token Formation Patterns:** *None successfully parsed*

### A。ただしB。 (A. Tadashi B)
**Original Formation String:** `Statement A + ただし + Condition B`
- **String Markers:** `ただし`
- **Token Formation Patterns:** *None successfully parsed*

### A。だが B。(~daga)
**Original Formation String:** `Sentence A + だが + Sentence B`
- **String Markers:** `だが`
- **Token Formation Patterns:** *None successfully parsed*

### A。だって B。(Datte~)
**Original Formation String:** `Verb-casual + だって、い-Adjective + だって、な-Adjective + だって、Noun + だって`
- **String Markers:** `だって`
- **Token Formation Patterns:**
  - [verb] + `だって` + [adjective] + `だって` + [adjective] + `だって` + [noun] + `だって`

### A。ちなみに B。(A. Chinamini B.)
**Original Formation String:** `A。ちなみに B。`
- **String Markers:** `ちなみに`
- **Token Formation Patterns:** *None successfully parsed*

### A。ということは B。 (A. To iu koto wa B.)
**Original Formation String:** `A + ということは + B`
- **String Markers:** `ということは`
- **Token Formation Patterns:** *None successfully parsed*

### A。というのは B。(Toiu no wa~)
**Original Formation String:** `[Statement A]。というのは、[Statement B]。`
- **String Markers:** `というのは`
- **Token Formation Patterns:** *None successfully parsed*

### A。なおB。(A. Nao B.)
**Original Formation String:** `A (sentence) + なお + B (sentence)`
- **String Markers:** `なお`
- **Token Formation Patterns:** *None successfully parsed*

### A。もっとも B。(Motto mo ~)
**Original Formation String:** `Clause A + もっとも + Clause B`
- **String Markers:** `もっとも`
- **Token Formation Patterns:** *None successfully parsed*

### A。要するに B。(A. Yousuru ni B.)
**Original Formation String:** `A。要するに B。`
- **String Markers:** `要するに`
- **Token Formation Patterns:** *None successfully parsed*

### Noun につき (〜ni tsuki)
**Original Formation String:** `Noun + につき`
- **String Markers:** `につき`
- **Token Formation Patterns:**
  - [noun] + `につき`

### Noun にて (Noun nite)
**Original Formation String:** `Noun + にて`
- **String Markers:** `にて`
- **Token Formation Patterns:**
  - [noun] + `にて`

### Noun の ことだから (Noun no koto dakara)
**Original Formation String:** `Noun + のことだから`
- **String Markers:** `のことだから`
- **Token Formation Patterns:**
  - [noun] + `のことだから`

### Noun を はじめ (Noun wo hajime)
**Original Formation String:** `Noun + をはじめ`
- **String Markers:** `をはじめ`
- **Token Formation Patterns:**
  - [noun] + `をはじめ`

### Noun を はじめとして (Noun wo hajime to shite)
**Original Formation String:** `Noun + をはじめとして`
- **String Markers:** `をはじめとして`
- **Token Formation Patterns:**
  - [noun] + `をはじめとして`

### Noun を はじめとする Noun (Noun o hajime to suru Noun)
**Original Formation String:** `Noun1 を はじめとする Noun2`
- **String Markers:** `をはじめとする`
- **Token Formation Patterns:**
  - [noun] + `を` + `はじめとする` + [noun]

### Noun を めぐって (Noun wo megutte)
**Original Formation String:** `Noun + を + めぐって`
- **String Markers:** `をめぐって`, `めぐって`
- **Token Formation Patterns:**
  - [noun] + `を` + `めぐって`

### Noun を めぐる Noun (Noun o meguru Noun)
**Original Formation String:** `Noun1 + を + めぐる + Noun2`
- **String Markers:** `をめぐる`, `めぐる`
- **Token Formation Patterns:**
  - [noun] + `を` + `めぐる` + [noun]

### Noun を もとに (Noun o moto ni)
**Original Formation String:** `Noun + をもとに`
- **String Markers:** `をもとに`
- **Token Formation Patterns:**
  - [noun] + `をもとに`

### Noun を もとにして (Noun wo moto ni shite)
**Original Formation String:** `Noun + をもとにして`
- **String Markers:** `をもとにして`
- **Token Formation Patterns:**
  - [noun] + `をもとにして`

### Verb ことなく (~kotonaku)
**Original Formation String:** `Verb-stem + ことなく`
- **String Markers:** `ことなく`
- **Token Formation Patterns:**
  - [verb] + `ことなく`

### Verb ないことには Verb ない (~nai koto ni wa ~ nai)
**Original Formation String:** `Verb-ない + ことには + Verb-ない`
- **String Markers:** `ないことには`, `ことには`
- **Token Formation Patterns:**
  - [verb] + `ことには` + [verb]

### 〜からして (〜kara shite)
**Original Formation String:** `Noun + からして`
- **String Markers:** `からして`
- **Token Formation Patterns:**
  - [noun] + `からして`

### 〜の上では (〜no ue de wa)
**Original Formation String:** `Noun or Phrase + の上では`
- **String Markers:** `の上では`
- **Token Formation Patterns:**
  - [noun] + `の上では`

### どうにか～ないものか (dō ni ka ~ nai mono ka)
**Original Formation String:** `どうにか + Verb-negative form + ないものか`
- **String Markers:** `どうにか`, `ないものか`
- **Token Formation Patterns:**
  - `どうにか` + [verb] + `ないものか`

### ～あげく (~ageku)
**Original Formation String:** `Verb-た + あげく / Noun + の + あげく`
- **String Markers:** `あげく`
- **Token Formation Patterns:**
  - [verb] + `あげく` + [noun] + `の` + `あげく`

### ～あまり (〜amari)
**Original Formation String:** `Verb-ます stem + あまり, い-Adjective + あまり, な-Adjective + のあまり, Noun + のあまり`
- **String Markers:** `あまり`, `のあまり`
- **Token Formation Patterns:**
  - [verb] + `あまり`
  - [adjective] + `あまり`
  - [adjective] + `のあまり`
  - [noun] + `のあまり`

### ～うちに (〜uchi ni)
**Original Formation String:** `Verb-casual + うちに, い-Adjective + うちに, な-Adjective + なうちに, Noun + のうちに`
- **String Markers:** `うちに`, `なうちに`, `のうちに`
- **Token Formation Patterns:**
  - [verb] + `うちに`
  - [adjective] + `うちに`
  - [adjective] + `なうちに`
  - [noun] + `のうちに`

### ～かいがあって (〜kaiga atte)
**Original Formation String:** `Verb-past + かいがあって / Noun + の + かいがあって`
- **String Markers:** `かいがあって`
- **Token Formation Patterns:**
  - [verb] + `かいがあって` + [noun] + `の` + `かいがあって`

### ～かいもなく (〜kai mo naku)
**Original Formation String:** `Verb-た + かいもなく / Noun + の + かいもなく`
- **String Markers:** `かいもなく`
- **Token Formation Patterns:**
  - [verb] + `かいもなく` + [noun] + `の` + `かいもなく`

### ～かける (〜kakeru)
**Original Formation String:** `Verb-stem + かける`
- **String Markers:** `かける`
- **Token Formation Patterns:**
  - [verb] + `かける`

### ～かねない (〜kane nai)
**Original Formation String:** `Verb-stem + かねない`
- **String Markers:** `かねない`
- **Token Formation Patterns:**
  - [verb] + `かねない`

### ～かねる (〜kaneru)
**Original Formation String:** `Verb-ます stem + かねる`
- **String Markers:** `かねる`
- **Token Formation Patterns:**
  - [verb] + `かねる`

### ～かのようだ (〜ka no you da)
**Original Formation String:** `Verb-casual + かのようだ, い-Adjective + かのようだ, な-Adjective + であるかのようだ, Noun + であるかのようだ`
- **String Markers:** `かのようだ`, `であるかのようだ`
- **Token Formation Patterns:**
  - [verb] + `かのようだ`
  - [adjective] + `かのようだ`
  - [adjective] + `であるかのようだ`
  - [noun] + `であるかのようだ`

### ～からこそ (〜kara koso)
**Original Formation String:** `Verb-casual + からこそ, い-Adjective + からこそ, な-Adjective + だからこそ, Noun + だからこそ`
- **String Markers:** `からこそ`, `だからこそ`
- **Token Formation Patterns:**
  - [verb] + `からこそ`
  - [adjective] + `からこそ`
  - [adjective] + `だからこそ`
  - [noun] + `だからこそ`

### ～からすると (〜kara suru to)
**Original Formation String:** `Noun + からすると`
- **String Markers:** `からすると`
- **Token Formation Patterns:**
  - [noun] + `からすると`

### ～からといって (〜kara to itte)
**Original Formation String:** `Verb-casual + からといって, い-Adjective + からといって, な-Adjective + だからといって, Noun + だからといって`
- **String Markers:** `からといって`, `だからといって`
- **Token Formation Patterns:**
  - [verb] + `からといって`
  - [adjective] + `からといって`
  - [adjective] + `だからといって`
  - [noun] + `だからといって`

### ～からには (〜kara niwa)
**Original Formation String:** `Noun + だ + からには, な-Adjective + だ + からには, い-Adjective + からには, Verb-casual + からには`
- **String Markers:** `からには`
- **Token Formation Patterns:**
  - [noun] + `だ` + `からには`
  - [adjective] + `だ` + `からには`
  - [adjective] + `からには`
  - [verb] + `からには`

### ～から見ると (〜kara miru to)
**Original Formation String:** `Noun + から見ると`
- **String Markers:** `から見ると`
- **Token Formation Patterns:**
  - [noun] + `から見ると`

### ～から言うと (〜kara iuto)
**Original Formation String:** `Noun + から言うと (common), [Verb-casual / Adjective + から言って] (less common)`
- **String Markers:** `から言うと`, `から言って`
- **Token Formation Patterns:**
  - [noun] + `から言うと` + [verb] + [adjective] + `から言って`

### ～から～にかけて (〜kara 〜ni kakete)
**Original Formation String:** `Noun 1 + から + Noun 2 + にかけて`
- **String Markers:** `から`, `にかけて`
- **Token Formation Patterns:**
  - [noun] + `から` + [noun] + `にかけて`

### ～か～ないかのうちに (〜ka〜naika no uchi ni)
**Original Formation String:** `Verb-casual + か + Verb-negative form + かのうちに`
- **String Markers:** `ないかのうちに`, `かのうちに`
- **Token Formation Patterns:**
  - [verb] + `か` + [verb] + `かのうちに`

### ～か～まいか (〜ka 〜maika)
**Original Formation String:** `Verb-volitional + か + Verb-volitional + まいか, い-Adjective + であるか + い-Adjective + であるまいか, な-Adjective + であるか + な-Adjective + であるまいか, Noun + であるか + Noun + であるまいか`
- **String Markers:** `まいか`, `であるか`, `であるまいか`
- **Token Formation Patterns:**
  - [verb] + `か` + [verb] + `まいか`
  - [adjective] + `であるか` + [adjective] + `であるまいか`
  - [adjective] + `であるか` + [adjective] + `であるまいか`
  - [noun] + `であるか` + [noun] + `であるまいか`

### ～がい (〜gai)
**Original Formation String:** `Verb-stem + がい`
- **String Markers:** `がい`
- **Token Formation Patterns:**
  - [verb] + `がい`

### ～がち (〜gachi)
**Original Formation String:** `Verb-ます stem + がち / い-Adjective stem + がち / な-Adjective stem + がち`
- **String Markers:** `がち`
- **Token Formation Patterns:**
  - [verb] + `がち` + [adjective] + `がち` + [adjective] + `がち`

### ～くせに (〜kuse ni)
**Original Formation String:** `Verb (casual) + くせに / い-Adjective + くせに / な-Adjective + な(or の) + くせに / Noun + の + くせに`
- **String Markers:** `くせに`
- **Token Formation Patterns:**
  - [verb] + `くせに` + [adjective] + `くせに` + [adjective] + `な` + `くせに` + [noun] + `の` + `くせに`

### ～ことから (〜koto kara)
**Original Formation String:** `Verb-casual + ことから / い-Adjective + ことから / な-Adjective + なことから / Noun + のことから`
- **String Markers:** `ことから`, `なことから`, `のことから`
- **Token Formation Patterns:**
  - [verb] + `ことから` + [adjective] + `ことから` + [adjective] + `なことから` + [noun] + `のことから`

### ～ことに (〜koto ni)
**Original Formation String:** `Verb-casual + ことに / い-Adjective + ことに / な-Adjective + なことに / Noun + のことに`
- **String Markers:** `ことに`, `なことに`, `のことに`
- **Token Formation Patterns:**
  - [verb] + `ことに` + [adjective] + `ことに` + [adjective] + `なことに` + [noun] + `のことに`

### ～ことになっている (〜koto ni natte iru)
**Original Formation String:** `Verb-plain form + ことになっている / い-Adjective + ことになっている / な-Adjective + だ + ことになっている / Noun + だ + ことになっている`
- **String Markers:** `ことになっている`
- **Token Formation Patterns:**
  - [verb] + `ことになっている` + [adjective] + `ことになっている` + [adjective] + `だ` + `ことになっている` + [noun] + `だ` + `ことになっている`

### ～さえ～ば (〜sae ~ba)
**Original Formation String:** `Noun + さえ + Verb-conditional / Verb-ますstem + さえすれば / etc. (varies by part of speech)`
- **String Markers:** `さえ`, `さえすれば`
- **Token Formation Patterns:**
  - [noun] + `さえ` + [verb] + [verb] + `さえすれば`

### ～ざるを得ない (〜zaru wo enai)
**Original Formation String:** `Verb-ない form (drop ない) + ざるを得ない`
- **String Markers:** `ざるを得ない`
- **Token Formation Patterns:**
  - [verb] + `ざるを得ない`

### ～ずにはいられない (〜zu ni wa irarenai)
**Original Formation String:** `Verb-ない form (drop ない) + ずにはいられない`
- **String Markers:** `ずにはいられない`
- **Token Formation Patterns:**
  - [verb] + `ずにはいられない`

### ～そうにない (〜sou ni nai)
**Original Formation String:** `Verb-stem + そうにない / い-Adjective (drop い) + そうにない / な-Adjective + そうにない`
- **String Markers:** `そうにない`
- **Token Formation Patterns:**
  - [verb] + `そうにない` + [adjective] + `そうにない` + [adjective] + `そうにない`

### ～たかと思ったら (〜ta ka to omottara)
**Original Formation String:** `Verb-た form + かと思ったら`
- **String Markers:** `たかと思ったら`, `かと思ったら`
- **Token Formation Patterns:**
  - [verb] + `かと思ったら`

### ～たきり (〜takiri)
**Original Formation String:** `Verb-past + きり`
- **String Markers:** `たきり`, `きり`
- **Token Formation Patterns:**
  - [verb] + `きり`

### ～たところ (〜ta tokoro)
**Original Formation String:** `Verb-past + ところ`
- **String Markers:** `たところ`, `ところ`
- **Token Formation Patterns:**
  - [verb] + `ところ`

### ～たとたん (〜ta totan)
**Original Formation String:** `Verb-past + たとたん`
- **String Markers:** `たとたん`
- **Token Formation Patterns:**
  - [verb] + `たとたん`

### ～だけあって (〜dake atte)
**Original Formation String:** `Verb-casual + だけあって, い-Adjective + だけあって, な-Adjective + なだけあって, Noun + だけあって`
- **String Markers:** `だけあって`, `なだけあって`
- **Token Formation Patterns:**
  - [verb] + `だけあって`
  - [adjective] + `だけあって`
  - [adjective] + `なだけあって`
  - [noun] + `だけあって`

### ～だけましだ (〜dake mashi da)
**Original Formation String:** `Verb-casual + だけましだ, い-Adjective + だけましだ, な-Adjective + だけましだ, Noun + だけましだ`
- **String Markers:** `だけましだ`
- **Token Formation Patterns:**
  - [verb] + `だけましだ`
  - [adjective] + `だけましだ`
  - [adjective] + `だけましだ`
  - [noun] + `だけましだ`

### ～だらけ (〜darake)
**Original Formation String:** `Noun + だらけ`
- **String Markers:** `だらけ`
- **Token Formation Patterns:**
  - [noun] + `だらけ`

### ～っこない (〜kkonai)
**Original Formation String:** `Verb-negative stem + っこない`
- **String Markers:** `っこない`
- **Token Formation Patterns:**
  - [verb] + `っこない`

### ～っぱなし (〜ppanashi)
**Original Formation String:** `Verb-ます stem + っぱなし`
- **String Markers:** `っぱなし`
- **Token Formation Patterns:**
  - [verb] + `っぱなし`

### ～っぽい (〜ppoi)
**Original Formation String:** `Noun + っぽい, Verb-casual + っぽい, い-Adjective + っぽい, な-Adjective + っぽい`
- **String Markers:** `っぽい`
- **Token Formation Patterns:**
  - [noun] + `っぽい`
  - [verb] + `っぽい`
  - [adjective] + `っぽい`
  - [adjective] + `っぽい`

### ～つつ (〜tsutsu)
**Original Formation String:** `Verb-stem + つつ`
- **String Markers:** `つつ`
- **Token Formation Patterns:**
  - [verb] + `つつ`

### ～つつある (〜tsutsu aru)
**Original Formation String:** `Verb-stem + つつある`
- **String Markers:** `つつある`
- **Token Formation Patterns:**
  - [verb] + `つつある`

### ～ていられない (〜te irarenai)
**Original Formation String:** `Verb-て form + いられない`
- **String Markers:** `ていられない`, `いられない`
- **Token Formation Patterns:**
  - [verb] + `いられない`

### ～てかなわない (〜te kanawanai)
**Original Formation String:** `Adjective (〜く / 〜で) + て + かなわない / Verb phrase (reworded to an adjective/negative) + て + かなわない`
- **String Markers:** `てかなわない`, `かなわない`
- **Token Formation Patterns:**
  - [adjective] + `て` + `かなわない` + [verb] + `て` + `かなわない`

### ～てからでないと (〜te kara denai to)
**Original Formation String:** `Verb-て + からでないと`
- **String Markers:** `てからでないと`, `からでないと`
- **Token Formation Patterns:**
  - [verb] + `からでないと`

### ～てこそ (〜te koso)
**Original Formation String:** `Verb-て form + こそ / い-Adjective + くてこそ / な-Adjective + でこそ / Noun + でこそ`
- **String Markers:** `てこそ`, `こそ`, `くてこそ`, `でこそ`
- **Token Formation Patterns:**
  - [verb] + `こそ` + [adjective] + `くてこそ` + [adjective] + `でこそ` + [noun] + `でこそ`

### ～てはならない (〜te wa naranai)
**Original Formation String:** `Verb-て form + はならない`
- **String Markers:** `てはならない`, `はならない`
- **Token Formation Patterns:**
  - [verb] + `はならない`

### ～てまで (〜te made)
**Original Formation String:** `Verb-て form + まで`
- **String Markers:** `てまで`, `まで`
- **Token Formation Patterns:**
  - [verb] + `まで`

### ～て当然だ (〜te tōzen da)
**Original Formation String:** `Verb-て form + 当然だ`
- **String Markers:** `て当然だ`, `当然だ`
- **Token Formation Patterns:**
  - [verb] + `当然だ`

### ～でしょうがない (〜deshou ga nai)
**Original Formation String:** `い-Adjective(く) + てしょうがない / な-Adjective + で(は)しょうがない / Verb-て form + しょうがない`
- **String Markers:** `でしょうがない`, `てしょうがない`, `ではしょうがない`, `しょうがない`
- **Token Formation Patterns:**
  - [adjective] + `てしょうがない` + [adjective] + `でしょうがない` + [verb] + `しょうがない`

### ～でたまらない (〜de tamaranai)
**Original Formation String:** `い-Adjective (く) + てたまらない / な-Adjective + でたまらない / Verb-て form + たまらない`
- **String Markers:** `でたまらない`, `てたまらない`, `たまらない`
- **Token Formation Patterns:**
  - [adjective] + `てたまらない` + [adjective] + `でたまらない` + [verb] + `たまらない`

### ～でならない (〜de naranai)
**Original Formation String:** `な-Adjective + でならない / い-Adjective (く) + てならない / Verb-て + ならない`
- **String Markers:** `でならない`, `てならない`, `ならない`
- **Token Formation Patterns:**
  - [adjective] + `でならない` + [adjective] + `てならない` + [verb] + `ならない`

### ～ではないか (〜de wa nai ka)
**Original Formation String:** `Noun + ではないか / い-Adjective + ではないか / な-Adjective + ではないか / Verb-casual + ではないか`
- **String Markers:** `ではないか`
- **Token Formation Patterns:**
  - [noun] + `ではないか` + [adjective] + `ではないか` + [adjective] + `ではないか` + [verb] + `ではないか`

### ～でばかりはいられない (〜de bakari wa irarenai)
**Original Formation String:** `Verb-て form + ばかりはいられない / Noun + ばかりはいられない (with appropriate particles)`
- **String Markers:** `でばかりはいられない`, `ばかりはいられない`
- **Token Formation Patterns:**
  - [verb] + `ばかりはいられない` + [noun] + `ばかりはいられない`

### ～というものだ (〜to iu mono da)
**Original Formation String:** `Sentence + というものだ`
- **String Markers:** `というものだ`
- **Token Formation Patterns:** *None successfully parsed*

### ～とおり (〜toori)
**Original Formation String:** `Verb-casual + とおり, い-Adjective + とおり, な-Adjective + だとおり, Noun + だとおり`
- **String Markers:** `とおり`, `だとおり`
- **Token Formation Patterns:**
  - [verb] + `とおり`
  - [adjective] + `とおり`
  - [adjective] + `だとおり`
  - [noun] + `だとおり`

### ～とか (〜to ka)
**Original Formation String:** `Verb-casual + とか, い-Adjective + とか, な-Adjective + だとか, Noun + だとか`
- **String Markers:** `とか`, `だとか`
- **Token Formation Patterns:**
  - [verb] + `とか`
  - [adjective] + `とか`
  - [adjective] + `だとか`
  - [noun] + `だとか`

### ～ところ (〜tokoro)
**Original Formation String:** `Verb-casual + ところ, い-Adjective + ところ, な-Adjective + なところ, Noun + のところ`
- **String Markers:** `ところ`, `なところ`, `のところ`
- **Token Formation Patterns:**
  - [verb] + `ところ`
  - [adjective] + `ところ`
  - [adjective] + `なところ`
  - [noun] + `のところ`

### ～としたら (〜to shitara)
**Original Formation String:** `Verb-casual + としたら, い-Adjective + としたら, な-Adjective + だとしたら, Noun + だとしたら`
- **String Markers:** `としたら`, `だとしたら`
- **Token Formation Patterns:**
  - [verb] + `としたら`
  - [adjective] + `としたら`
  - [adjective] + `だとしたら`
  - [noun] + `だとしたら`

### ～としても (〜to shite mo)
**Original Formation String:** `Verb-casual + としても, い-Adjective + としても, な-Adjective + だとしても, Noun + だとしても`
- **String Markers:** `としても`, `だとしても`
- **Token Formation Patterns:**
  - [verb] + `としても`
  - [adjective] + `としても`
  - [adjective] + `だとしても`
  - [noun] + `だとしても`

### ～とは限らない (〜to wa kagiranai)
**Original Formation String:** `Verb-casual + とは限らない, い-Adjective + とは限らない, な-Adjective + だとは限らない, Noun + だとは限らない`
- **String Markers:** `とは限らない`, `だとは限らない`
- **Token Formation Patterns:**
  - [verb] + `とは限らない`
  - [adjective] + `とは限らない`
  - [adjective] + `だとは限らない`
  - [noun] + `だとは限らない`

### ～と～ともに (〜to 〜tomoni)
**Original Formation String:** `Verb-casual + とともに, い-Adjective + とともに, な-Adjective + とともに, Noun + とともに`
- **String Markers:** `ともに`, `とともに`
- **Token Formation Patterns:**
  - [verb] + `とともに`
  - [adjective] + `とともに`
  - [adjective] + `とともに`
  - [noun] + `とともに`

### ～どころか (〜dokoro ka)
**Original Formation String:** `Verb-casual + どころか, い-Adjective + どころか, な-Adjective + どころか, Noun + どころか`
- **String Markers:** `どころか`
- **Token Formation Patterns:**
  - [verb] + `どころか`
  - [adjective] + `どころか`
  - [adjective] + `どころか`
  - [noun] + `どころか`

### ～どころではない (〜dokoro de wa nai)
**Original Formation String:** `Verb-casual + どころではない, い-Adjective + どころではない, な-Adjective + どころではない, Noun + どころではない`
- **String Markers:** `どころではない`
- **Token Formation Patterns:**
  - [verb] + `どころではない`
  - [adjective] + `どころではない`
  - [adjective] + `どころではない`
  - [noun] + `どころではない`

### ～ないことはない (〜nai koto wa nai)
**Original Formation String:** `Verb-ないform + ことはない`
- **String Markers:** `ないことはない`, `ことはない`
- **Token Formation Patterns:**
  - [verb] + `ことはない`

### ～ないこともない (〜nai koto mo nai)
**Original Formation String:** `Verb-ないForm + こともない, い-adjective + こともない`
- **String Markers:** `ないこともない`, `こともない`
- **Token Formation Patterns:**
  - [verb] + `こともない` + `い` + `こともない`

### ～ないではいられない (〜nai de wa irarenai)
**Original Formation String:** `Verb-ない form + ではいられない or じゃいられない`
- **String Markers:** `ないではいられない`, `ではいられない`, `じゃいられない`
- **Token Formation Patterns:**
  - [verb] + `ではいられない` + `じゃいられない`

### ～ながら (〜nagara)
**Original Formation String:** `Verb-stem + ながら`
- **String Markers:** `ながら`
- **Token Formation Patterns:**
  - [verb] + `ながら`

### ～にあたり (〜ni atari)
**Original Formation String:** `Noun + にあたり`
- **String Markers:** `にあたり`
- **Token Formation Patterns:**
  - [noun] + `にあたり`

### ～において (〜ni oite)
**Original Formation String:** `Noun + において`
- **String Markers:** `において`
- **Token Formation Patterns:**
  - [noun] + `において`

### ～にかかわらず (〜ni kakawarazu)
**Original Formation String:** `Verb-dictionary form + にかかわらず, い-Adjective + にかかわらず, な-Adjective + にかかわらず, Noun + にかかわらず`
- **String Markers:** `にかかわらず`
- **Token Formation Patterns:**
  - [verb] + `にかかわらず`
  - [adjective] + `にかかわらず`
  - [adjective] + `にかかわらず`
  - [noun] + `にかかわらず`

### ～にかけては (〜ni kakete wa)
**Original Formation String:** `Noun + にかけては`
- **String Markers:** `にかけては`
- **Token Formation Patterns:**
  - [noun] + `にかけては`

### ～にしたがって (〜ni shitagatte)
**Original Formation String:** `Noun + にしたがって`
- **String Markers:** `にしたがって`
- **Token Formation Patterns:**
  - [noun] + `にしたがって`

### ～にしたら (〜ni shitara)
**Original Formation String:** `Noun + にしたら, Pronoun + にしたら`
- **String Markers:** `にしたら`
- **Token Formation Patterns:**
  - [noun] + `にしたら` + `にしたら`

### ～にしろ～にしろ (〜ni shiro 〜ni shiro)
**Original Formation String:** `Verb (dictionary form or negative form) + にしろ, い-Adjective + にしろ, な-Adjective + にしろ, Noun + にしろ`
- **String Markers:** `にしろ`
- **Token Formation Patterns:**
  - [verb] + `にしろ`
  - [adjective] + `にしろ`
  - [adjective] + `にしろ`
  - [noun] + `にしろ`

### ～につけ～につけ (〜ni tsuke 〜ni tsuke)
**Original Formation String:** `Verb-casual + につけ, い-Adjective + につけ, な-Adjective + につけ, Noun + につけ`
- **String Markers:** `につけ`
- **Token Formation Patterns:**
  - [verb] + `につけ`
  - [adjective] + `につけ`
  - [adjective] + `につけ`
  - [noun] + `につけ`

### ～につれて (〜ni tsurete)
**Original Formation String:** `Verb (dictionary form) + につれて, Noun + につれて`
- **String Markers:** `につれて`
- **Token Formation Patterns:**
  - [verb] + `につれて`
  - [noun] + `につれて`

### ～にともなって (〜ni tomonatte)
**Original Formation String:** `Noun (event) + にともなって, Verb-casual + にともなって`
- **String Markers:** `にともなって`
- **Token Formation Patterns:**
  - [noun] + `にともなって`
  - [verb] + `にともなって`

### ～にほかならない (〜ni hoka naranai)
**Original Formation String:** `Verb-plain + にほかならない, い-Adjective + にほかならない, な-Adjective + にほかならない, Noun + にほかならない`
- **String Markers:** `にほかならない`
- **Token Formation Patterns:**
  - [verb] + `にほかならない`
  - [adjective] + `にほかならない`
  - [adjective] + `にほかならない`
  - [noun] + `にほかならない`

### ～にもかかわらず (〜ni mo kakawarazu)
**Original Formation String:** `Verb (any tense/form) + にもかかわらず, い-Adjective + にもかかわらず, な-Adjective (or Noun) + であるにもかかわらず`
- **String Markers:** `にもかかわらず`, `であるにもかかわらず`
- **Token Formation Patterns:**
  - [verb] + `にもかかわらず`
  - [adjective] + `にもかかわらず`
  - [adjective] + [noun] + `であるにもかかわらず`

### ～により (〜ni yori)
**Original Formation String:** `Noun + により, Verb + により`
- **String Markers:** `により`
- **Token Formation Patterns:**
  - [noun] + `により`
  - [verb] + `により`

### ～にわたって (〜ni watatte)
**Original Formation String:** `Noun + にわたって`
- **String Markers:** `にわたって`
- **Token Formation Patterns:**
  - [noun] + `にわたって`

### ～に先立ち (〜ni sakidachi)
**Original Formation String:** `Noun + に先立ち / Verb-dictionary form + に先立って`
- **String Markers:** `に先立ち`, `に先立って`
- **Token Formation Patterns:**
  - [noun] + `に先立ち` + [verb] + `に先立って`

### ～に反して (〜ni hanshite)
**Original Formation String:** `Noun + に反して`
- **String Markers:** `に反して`
- **Token Formation Patterns:**
  - [noun] + `に反して`

### ～に基づいて (〜ni motozuite)
**Original Formation String:** `Noun + に基づいて`
- **String Markers:** `に基づいて`
- **Token Formation Patterns:**
  - [noun] + `に基づいて`

### ～に対して (〜ni taishite)
**Original Formation String:** `Noun + に対して`
- **String Markers:** `に対して`
- **Token Formation Patterns:**
  - [noun] + `に対して`

### ～に応えて (〜ni kotaete)
**Original Formation String:** `Noun + に応えて`
- **String Markers:** `に応えて`
- **Token Formation Patterns:**
  - [noun] + `に応えて`

### ～に応じて (〜ni oujite)
**Original Formation String:** `Noun + に応じて`
- **String Markers:** `に応じて`
- **Token Formation Patterns:**
  - [noun] + `に応じて`

### ～に決まっている (〜ni kimatte iru)
**Original Formation String:** `Verb-casual + に決まっている, い-Adjective + に決まっている, な-Adjective + だに決まっている, Noun + だに決まっている`
- **String Markers:** `に決まっている`, `だに決まっている`
- **Token Formation Patterns:**
  - [verb] + `に決まっている`
  - [adjective] + `に決まっている`
  - [adjective] + `だに決まっている`
  - [noun] + `だに決まっている`

### ～に沿って (〜ni sotte)
**Original Formation String:** `Noun + に沿って`
- **String Markers:** `に沿って`
- **Token Formation Patterns:**
  - [noun] + `に沿って`

### ～に過ぎない (〜ni suginai)
**Original Formation String:** `Verb-casual + に過ぎない, い-Adjective + に過ぎない, な-Adjective + に過ぎない, Noun + に過ぎない`
- **String Markers:** `に過ぎない`
- **Token Formation Patterns:**
  - [verb] + `に過ぎない`
  - [adjective] + `に過ぎない`
  - [adjective] + `に過ぎない`
  - [noun] + `に過ぎない`

### ～に関わって (〜ni kakawatte)
**Original Formation String:** `Verb-casual + に関わって, い-Adjective + に関わって, な-Adjective + に関わって, Noun + に関わって`
- **String Markers:** `に関わって`
- **Token Formation Patterns:**
  - [verb] + `に関わって`
  - [adjective] + `に関わって`
  - [adjective] + `に関わって`
  - [noun] + `に関わって`

### ～に限り (〜ni kagiri)
**Original Formation String:** `Noun + に限り`
- **String Markers:** `に限り`
- **Token Formation Patterns:**
  - [noun] + `に限り`

### ～に際して (〜ni saishite)
**Original Formation String:** `Noun + に際して`
- **String Markers:** `に際して`
- **Token Formation Patterns:**
  - [noun] + `に際して`

### ～ねばならない (〜neba naranai)
**Original Formation String:** `Verb-ない form → (remove い) → ね + ばならない`
- **String Markers:** `ねばならない`, `ばならない`
- **Token Formation Patterns:**
  - [verb] + `ね` + `ばならない`

### ～のみならず～も (〜nomi narazu 〜mo)
**Original Formation String:** `Verb-casual + のみならず + (も), い-Adjective + のみならず + (も), な-Adjective + のみならず + (も), Noun + のみならず + (も)`
- **String Markers:** `のみならず`
- **Token Formation Patterns:**
  - [verb] + `のみならず`
  - [adjective] + `のみならず`
  - [adjective] + `のみならず`
  - [noun] + `のみならず`

### ～のももっともだ (〜no mo mottomo da)
**Original Formation String:** `Verb-casual + のももっともだ, い-Adjective + のももっともだ, な-Adjective + なのももっともだ, Noun + なのももっともだ`
- **String Markers:** `のももっともだ`, `なのももっともだ`
- **Token Formation Patterns:**
  - [verb] + `のももっともだ`
  - [adjective] + `のももっともだ`
  - [adjective] + `なのももっともだ`
  - [noun] + `なのももっともだ`

### ～の下で (〜no shita de)
**Original Formation String:** `Verb-casual + の下で, い-Adjective + の下で, な-Adjective + の下で, Noun + の下で`
- **String Markers:** `の下で`
- **Token Formation Patterns:**
  - [verb] + `の下で`
  - [adjective] + `の下で`
  - [adjective] + `の下で`
  - [noun] + `の下で`

### ～はともかく～は (〜wa tomokaku 〜wa)
**Original Formation String:** `Noun1 はともかく Noun2 は`
- **String Markers:** `はともかく`
- **Token Formation Patterns:**
  - [noun] + `はともかく` + [noun] + `は`

### ～はまだしも (〜wa mada shimo)
**Original Formation String:** `Noun1 + はまだしも + Noun2`
- **String Markers:** `はまだしも`
- **Token Formation Patterns:**
  - [noun] + `はまだしも` + [noun]

### ～はもとより (〜wa moto yori)
**Original Formation String:** `Noun1 + はもとより, Noun2 + も`
- **String Markers:** `はもとより`
- **Token Formation Patterns:**
  - [noun] + `はもとより`
  - [noun] + `も`

### ～は抜きにして (〜wa nuki ni shite)
**Original Formation String:** `Noun + は抜きにして`
- **String Markers:** `は抜きにして`
- **Token Formation Patterns:**
  - [noun] + `は抜きにして`

### ～ばかりか〜も (〜bakari ka 〜 mo)
**Original Formation String:** `Noun/Verb/Adjective + ばかりか + Noun/Verb/Adjective + も`
- **String Markers:** `ばかりか`
- **Token Formation Patterns:**
  - [noun] + [verb] + [adjective] + `ばかりか` + [noun] + [verb] + [adjective] + `も`

### ～ばかりだ (〜bakari da)
**Original Formation String:** `Verb-てform + ばかりだ, い-Adjective + ばかりだ, な-Adjective + ばかりだ, Noun + ばかりだ`
- **String Markers:** `ばかりだ`
- **Token Formation Patterns:**
  - [verb] + `ばかりだ`
  - [adjective] + `ばかりだ`
  - [adjective] + `ばかりだ`
  - [noun] + `ばかりだ`

### ～ばかりに (〜bakari ni)
**Original Formation String:** `Verb-casual + ばかりに, い-Adjective + ばかりに, な-Adjective + なばかりに, Noun + なばかりに`
- **String Markers:** `ばかりに`, `なばかりに`
- **Token Formation Patterns:**
  - [verb] + `ばかりに`
  - [adjective] + `ばかりに`
  - [adjective] + `なばかりに`
  - [noun] + `なばかりに`

### ～ば～というものでもない (〜ba 〜to iu mono demo nai)
**Original Formation String:** `Verb-ば form + というものでもない`
- **String Markers:** `というものでもない`
- **Token Formation Patterns:**
  - [verb] + `というものでもない`

### ～べきではない (〜beki dewa nai)
**Original Formation String:** `Verb-dictionary form + べき + ではない`
- **String Markers:** `べきではない`, `べき`, `ではない`
- **Token Formation Patterns:**
  - [verb] + `べき` + `ではない`

### ～まい (〜mai)
**Original Formation String:** `Verb-dictionary form + まい`
- **String Markers:** `まい`
- **Token Formation Patterns:**
  - [verb] + `まい`

### ～まで～て (〜made 〜te)
**Original Formation String:** `Time/Noun + まで + Verb(て-form)`
- **String Markers:** `まで`
- **Token Formation Patterns:**
  - [noun] + `まで` + [verb]

### ～ままに (〜mama ni)
**Original Formation String:** `Verb-て + まま, い-Adjective + のまま, な-Adjective + なまま, Noun + のまま`
- **String Markers:** `ままに`, `まま`, `のまま`, `なまま`
- **Token Formation Patterns:**
  - [verb] + `まま`
  - [adjective] + `のまま`
  - [adjective] + `なまま`
  - [noun] + `のまま`

### ～もかまわず (〜mo kamawazu)
**Original Formation String:** `Verb-dictionary form + もかまわず, Noun + もかまわず`
- **String Markers:** `もかまわず`
- **Token Formation Patterns:**
  - [verb] + `もかまわず`
  - [noun] + `もかまわず`

### ～ものか (〜mono ka)
**Original Formation String:** `Verb-casual + ものか, い-Adjective + ものか, な-Adjective + (な)ものか, Noun + (な)ものか`
- **String Markers:** `ものか`, `なものか`
- **Token Formation Patterns:**
  - [verb] + `ものか`
  - [adjective] + `ものか`
  - [adjective] + `ものか`
  - [noun] + `ものか`

### ～ものがある (〜mono ga aru)
**Original Formation String:** `Verb-casual + ものがある, い-Adjective + ものがある, な-Adjective + なものがある`
- **String Markers:** `ものがある`, `なものがある`
- **Token Formation Patterns:**
  - [verb] + `ものがある`
  - [adjective] + `ものがある`
  - [adjective] + `なものがある`

### ～ものだ (〜mono da)
**Original Formation String:** `Verb-dictionary form + ものだ, な-Adjective + なものだ, (Also: Verb-た form + ものだ for recollections)`
- **String Markers:** `ものだ`, `なものだ`
- **Token Formation Patterns:**
  - [verb] + `ものだ`
  - [adjective] + `なものだ` + [verb] + `ものだ`

### ～ものだから (〜mono dakara)
**Original Formation String:** `Verb-plain + ものだから, い-Adjective + ものだから, な-Adjective + なものだから, Noun + なものだから`
- **String Markers:** `ものだから`, `なものだから`
- **Token Formation Patterns:**
  - [verb] + `ものだから`
  - [adjective] + `ものだから`
  - [adjective] + `なものだから`
  - [noun] + `なものだから`

### ～ものではない (〜mono dewa nai)
**Original Formation String:** `Verb-dictionary form + ものではない`
- **String Markers:** `ものではない`
- **Token Formation Patterns:**
  - [verb] + `ものではない`

### ～ものなら (〜mono nara)
**Original Formation String:** `Verb-(potential/plain) form + ものなら, etc.`
- **String Markers:** `ものなら`
- **Token Formation Patterns:**
  - [verb] + `ものなら`

### ～ものの、～ (〜mono no、～)
**Original Formation String:** `Verb-casual + ものの, い-Adjective + ものの, な-Adjective + なものの, Noun + であるものの`
- **String Markers:** `ものの`, `なものの`, `であるものの`
- **Token Formation Patterns:**
  - [verb] + `ものの`
  - [adjective] + `ものの`
  - [adjective] + `なものの`
  - [noun] + `であるものの`

### ～も同然だ (〜mo douzen da)
**Original Formation String:** `Noun + (も)同然だ, Verb-casual + (も)同然だ, etc.`
- **String Markers:** `も同然だ`, `同然だ`
- **Token Formation Patterns:**
  - [noun] + `同然だ`
  - [verb] + `同然だ`

### ～やら～やら (〜yara〜yara)
**Original Formation String:** `Verb-casual + やら, い-Adjective + やら, な-Adjective + やら, Noun + やら`
- **String Markers:** `やら`
- **Token Formation Patterns:**
  - [verb] + `やら`
  - [adjective] + `やら`
  - [adjective] + `やら`
  - [noun] + `やら`

### ～ようがない (〜you ga nai)
**Original Formation String:** `Verb-ます stem + ようがない`
- **String Markers:** `ようがない`
- **Token Formation Patterns:**
  - [verb] + `ようがない`

### ～よりほかない (〜yori hoka nai)
**Original Formation String:** `Verb-dictionary form + よりほかない`
- **String Markers:** `よりほかない`
- **Token Formation Patterns:**
  - [verb] + `よりほかない`

### ～わけがない (〜wake ga nai)
**Original Formation String:** `Verb-casual + わけがない, い-Adjective + わけがない, な-Adjective + なわけがない, Noun + のわけがない`
- **String Markers:** `わけがない`, `なわけがない`, `のわけがない`
- **Token Formation Patterns:**
  - [verb] + `わけがない`
  - [adjective] + `わけがない`
  - [adjective] + `なわけがない`
  - [noun] + `のわけがない`

### ～わけだ (〜wake da)
**Original Formation String:** `Verb-casual + わけだ, い-Adjective + わけだ, な-Adjective + なわけだ, Noun + のわけだ`
- **String Markers:** `わけだ`, `なわけだ`, `のわけだ`
- **Token Formation Patterns:**
  - [verb] + `わけだ`
  - [adjective] + `わけだ`
  - [adjective] + `なわけだ`
  - [noun] + `のわけだ`

### ～わけではない (〜wake dewa nai)
**Original Formation String:** `Verb-plain + わけではない, い-Adjective + わけではない, な-Adjective + だわけではない, Noun + だわけではない`
- **String Markers:** `わけではない`, `だわけではない`
- **Token Formation Patterns:**
  - [verb] + `わけではない`
  - [adjective] + `わけではない`
  - [adjective] + `だわけではない`
  - [noun] + `だわけではない`

### ～わけにはいかない (〜wake ni wa ikanai)
**Original Formation String:** `Verb-dictionary form + わけにはいかない`
- **String Markers:** `わけにはいかない`
- **Token Formation Patterns:**
  - [verb] + `わけにはいかない`

### ～をきっかけに (〜wo kikkake ni)
**Original Formation String:** `Noun + をきっかけに`
- **String Markers:** `をきっかけに`
- **Token Formation Patterns:**
  - [noun] + `をきっかけに`

### ～を中心に (〜wo chuushin ni)
**Original Formation String:** `Noun + を中心に`
- **String Markers:** `を中心に`
- **Token Formation Patterns:**
  - [noun] + `を中心に`

### ～を問わず (〜wo towazu)
**Original Formation String:** `Noun + を問わず`
- **String Markers:** `を問わず`
- **Token Formation Patterns:**
  - [noun] + `を問わず`

### ～を込めて (〜wo komete)
**Original Formation String:** `Feeling/emotion/intention Noun + を + 込めて + Verb`
- **String Markers:** `を込めて`, `込めて`
- **Token Formation Patterns:**
  - [noun] + `を` + `込めて` + [verb]

### ～を通じて (〜wo tsuujite)
**Original Formation String:** `Noun + を通じて`
- **String Markers:** `を通じて`
- **Token Formation Patterns:**
  - [noun] + `を通じて`

### ～を頼りに (〜wo tayori ni)
**Original Formation String:** `Noun + を頼りに`
- **String Markers:** `を頼りに`
- **Token Formation Patterns:**
  - [noun] + `を頼りに`

### ～を～として (〜wo〜toshite)
**Original Formation String:** `Noun1 + を + Noun2 + として`
- **String Markers:** `として`
- **Token Formation Patterns:**
  - [noun] + `を` + [noun] + `として`

### ～一方 (〜ippou)
**Original Formation String:** `Verb-casual + 一方(で), い-Adjective + 一方(で), な-Adjective + な/である一方(で), Noun + である一方(で)`
- **String Markers:** `一方`, `一方で`, `である一方で`, `である一方`
- **Token Formation Patterns:**
  - [verb] + `一方`
  - [adjective] + `一方`
  - [adjective] + `な` + `である一方`
  - [noun] + `である一方`

### ～一方だ (〜ippou da)
**Original Formation String:** `Verb-dictionary form + 一方だ`
- **String Markers:** `一方だ`
- **Token Formation Patterns:**
  - [verb] + `一方だ`

### ～上で (〜ue de)
**Original Formation String:** `Verb-ますstem + 上で, Noun + の上で`
- **String Markers:** `上で`, `の上で`
- **Token Formation Patterns:**
  - [verb] + `上で`
  - [noun] + `の上で`

### ～上に (〜ue ni)
**Original Formation String:** `Verb-plain + 上に, い-Adjective + 上に, な-Adjective + な上に, Noun + の上に`
- **String Markers:** `上に`, `な上に`, `の上に`
- **Token Formation Patterns:**
  - [verb] + `上に`
  - [adjective] + `上に`
  - [adjective] + `な上に`
  - [noun] + `の上に`

### ～上は (～ue wa)
**Original Formation String:** `Verb-casual + 上は, い-Adjective + 上は, な-Adjective + な上は, Noun + の上は`
- **String Markers:** `上は`, `な上は`, `の上は`
- **Token Formation Patterns:**
  - [verb] + `上は`
  - [adjective] + `上は`
  - [adjective] + `な上は`
  - [noun] + `の上は`

### ～以上 (〜ijou)
**Original Formation String:** `Verb-casual + 以上, い-Adjective + 以上, な-Adjective + な以上, Noun + の以上`
- **String Markers:** `以上`, `な以上`, `の以上`
- **Token Formation Patterns:**
  - [verb] + `以上`
  - [adjective] + `以上`
  - [adjective] + `な以上`
  - [noun] + `の以上`

### ～以来 (〜irai)
**Original Formation String:** `Verb-past + 以来, い-Adjective + 以来, Noun + 以来`
- **String Markers:** `以来`
- **Token Formation Patterns:**
  - [verb] + `以来`
  - [adjective] + `以来`
  - [noun] + `以来`

### ～切る (〜kiru)
**Original Formation String:** `Verb-stem + 切る`
- **String Markers:** `切る`
- **Token Formation Patterns:**
  - [verb] + `切る`

### ～反面 (〜hanmen)
**Original Formation String:** `Verb-casual + 反面, い-Adjective + 反面, な-Adjective + である反面, Noun + である反面`
- **String Markers:** `反面`, `である反面`
- **Token Formation Patterns:**
  - [verb] + `反面`
  - [adjective] + `反面`
  - [adjective] + `である反面`
  - [noun] + `である反面`

### ～向け (〜muke)
**Original Formation String:** `Noun + 向け`
- **String Markers:** `向け`
- **Token Formation Patterns:**
  - [noun] + `向け`

### ～恐れがある (〜osore ga aru)
**Original Formation String:** `Verb-dictionary form + 恐れがある`
- **String Markers:** `恐れがある`
- **Token Formation Patterns:**
  - [verb] + `恐れがある`

### ～折には (〜ori ni wa)
**Original Formation String:** `Verb-dictionary form + 折には, Verb-た form + 折には, い-Adjective + 折には, な-Adjective + な折には, Noun + の折には`
- **String Markers:** `折には`, `な折には`, `の折には`
- **Token Formation Patterns:**
  - [verb] + `折には`
  - [verb] + `折には`
  - [adjective] + `折には`
  - [adjective] + `な折には`
  - [noun] + `の折には`

### ～次第 (〜shidai)
**Original Formation String:** `Verb-ますstem + 次第, Noun + 次第`
- **String Markers:** `次第`
- **Token Formation Patterns:**
  - [verb] + `次第`
  - [noun] + `次第`

### ～次第で (〜shidai de)
**Original Formation String:** `Noun + 次第で`
- **String Markers:** `次第で`
- **Token Formation Patterns:**
  - [noun] + `次第で`

### ～次第です (〜shidai desu)
**Original Formation String:** `Verb-ますstem + 次第です (or Noun + 次第です)`
- **String Markers:** `次第です`
- **Token Formation Patterns:**
  - [verb] + `次第です` + [noun] + `次第です`

### ～気味 (〜gimi)
**Original Formation String:** `Noun + 気味 (e.g., 風邪気味, 寝不足気味, 緊張気味)`
- **String Markers:** `気味`, `風邪気味`, `寝不足気味`, `緊張気味`
- **Token Formation Patterns:**
  - [noun] + `気味`

### ～限り (〜kagiri)
**Original Formation String:** `Verb-casual + 限り, い-Adjective + 限り, な-Adjective + な限り, Noun + の限り`
- **String Markers:** `限り`, `な限り`, `の限り`
- **Token Formation Patterns:**
  - [verb] + `限り`
  - [adjective] + `限り`
  - [adjective] + `な限り`
  - [noun] + `の限り`

### ～際に (〜sai ni)
**Original Formation String:** `Verb-casual + 際に, い-Adjective + 際に, な-Adjective + な際に, Noun + の際に`
- **String Markers:** `際に`, `な際に`, `の際に`
- **Token Formation Patterns:**
  - [verb] + `際に`
  - [adjective] + `際に`
  - [adjective] + `な際に`
  - [noun] + `の際に`

## N1

### A うが B うが (A uga B uga)
**Original Formation String:** `Verb-volitional form + うが + Verb-volitional form + うが, or Adjective (-かろう) + が + Adjective (-かろう) + が`
- **String Markers:** `うが`, `かろう`
- **Token Formation Patterns:**
  - [verb] + `うが` + [verb] + `うが` + [adjective] + `が` + [adjective] + `が`

### A うと B うと (A uto B uto)
**Original Formation String:** `い-adjective (-かろう) + と, な-adjective / Noun + であろうと`
- **String Markers:** `うと`, `かろう`, `であろうと`
- **Token Formation Patterns:**
  - `い` + `と` + `な` + [noun] + `であろうと`

### A かたわら B (A katawara B)
**Original Formation String:** `Verb-dictionary form + かたわら, Noun + のかたわら`
- **String Markers:** `かたわら`, `のかたわら`
- **Token Formation Patterns:**
  - [verb] + `かたわら`
  - [noun] + `のかたわら`

### A かれ B かれ (A kare B kare)
**Original Formation String:** `Commonly i-adjective stems + かれ + i-adjective stems + かれ (e.g. 早かれ遅かれ). Also sometimes Noun + かれ + Noun + かれ in older usage.`
- **String Markers:** `かれ`, `早かれ遅かれ`
- **Token Formation Patterns:**
  - `かれ` + `かれ` + [noun] + `かれ` + [noun] + `かれ`

### A だの B だの (A dano B dano)
**Original Formation String:** `Noun/Verb casual + だの + Noun/Verb casual + だの`
- **String Markers:** `だの`
- **Token Formation Patterns:**
  - [noun] + [verb] + `だの` + [noun] + [verb] + `だの`

### A であれ B であれ (A deare B deare)
**Original Formation String:** `Noun A + であれ + Noun B + であれ`
- **String Markers:** `であれ`
- **Token Formation Patterns:**
  - [noun] + `であれ` + [noun] + `であれ`

### A というか B というか (A to iu ka B to iu ka)
**Original Formation String:** `Phrase A + というか + Phrase B + というか`
- **String Markers:** `というか`
- **Token Formation Patterns:** *None successfully parsed*

### A とも B とも (A tomo B tomo)
**Original Formation String:** `Noun + とも + Noun + とも (or sometimes Verb forms for each A, B)`
- **String Markers:** `とも`
- **Token Formation Patterns:**
  - [noun] + `とも` + [noun] + `とも` + [verb]

### A にしろ B にしろ (A nishiro B nishiro)
**Original Formation String:** `Noun A + にしろ + Noun B + にしろ, or Verb-casual A + にしろ + Verb-casual B + にしろ`
- **String Markers:** `にしろ`
- **Token Formation Patterns:**
  - [noun] + `にしろ` + [noun] + `にしろ` + [verb] + `にしろ` + [verb] + `にしろ`

### A にせよ B にせよ (A ni seyo B ni seyo)
**Original Formation String:** `Noun + にせよ + Noun + にせよ (also works with verbs in dictionary form + にせよ)`
- **String Markers:** `にせよ`
- **Token Formation Patterns:**
  - [noun] + `にせよ` + [noun] + `にせよ` + `にせよ`

### A につけ B につけ (A ni tsuke B ni tsuke)
**Original Formation String:** `Phrase A (dictionary/adjective form) + につけ、Phrase B (dictionary/adjective form) + につけ`
- **String Markers:** `につけ`
- **Token Formation Patterns:** *None successfully parsed*

### A のやら B のやら (A no yara B no yara)
**Original Formation String:** `Noun1 + のやら + Noun2 + のやら (also works with adjectives and verbs + のやら)`
- **String Markers:** `のやら`
- **Token Formation Patterns:**
  - [noun] + `のやら` + [noun] + `のやら` + `のやら`

### Noun + あっての + Noun (A atte no B)
**Original Formation String:** `Noun1 + あっての + Noun2`
- **String Markers:** `あっての`
- **Token Formation Patterns:**
  - [noun] + `あっての` + [noun]

### Noun + ぐるみ (〜gurumi)
**Original Formation String:** `Noun + ぐるみ`
- **String Markers:** `ぐるみ`
- **Token Formation Patterns:**
  - [noun] + `ぐるみ`

### Noun + というもの (~ to iu mono)
**Original Formation String:** `Noun + というもの`
- **String Markers:** `というもの`
- **Token Formation Patterns:**
  - [noun] + `というもの`

### Noun + ときたら (〜tokitara)
**Original Formation String:** `Noun + ときたら`
- **String Markers:** `ときたら`
- **Token Formation Patterns:**
  - [noun] + `ときたら`

### Noun + ともあろう + Noun (~tomoarou~)
**Original Formation String:** `Noun + ともあろう + Noun`
- **String Markers:** `ともあろう`
- **Token Formation Patterns:**
  - [noun] + `ともあろう` + [noun]

### Noun + ならでは (~nara de wa)
**Original Formation String:** `Noun + ならでは`
- **String Markers:** `ならでは`
- **Token Formation Patterns:**
  - [noun] + `ならでは`

### Noun + ぬいて（~nuite)
**Original Formation String:** `Noun + ぬいて`
- **String Markers:** `ぬいて`
- **Token Formation Patterns:**
  - [noun] + `ぬいて`

### Noun + はどうであれ (~ wa dou de are)
**Original Formation String:** `Noun + はどうであれ`
- **String Markers:** `はどうであれ`
- **Token Formation Patterns:**
  - [noun] + `はどうであれ`

### Noun + 前提で (Noun + zentei de)
**Original Formation String:** `Noun + 前提で`
- **String Markers:** `前提で`
- **Token Formation Patterns:**
  - [noun] + `前提で`

### Noun かたがた (Noun kata gata)
**Original Formation String:** `Noun + かたがた`
- **String Markers:** `かたがた`
- **Token Formation Patterns:**
  - [noun] + `かたがた`

### Noun からある (〜kara aru)
**Original Formation String:** `Number + Counter + からある`
- **String Markers:** `からある`
- **Token Formation Patterns:** *None successfully parsed*

### Noun からする (Noun kara suru)
**Original Formation String:** `Noun + からする`
- **String Markers:** `からする`
- **Token Formation Patterns:**
  - [noun] + `からする`

### Noun からの (~kara no)
**Original Formation String:** `Noun + からの`
- **String Markers:** `からの`
- **Token Formation Patterns:**
  - [noun] + `からの`

### Noun から言わせれば (~kara iwasereba)
**Original Formation String:** `Noun + から言わせれば`
- **String Markers:** `から言わせれば`
- **Token Formation Patterns:**
  - [noun] + `から言わせれば`

### Noun がてら (Noun gatera)
**Original Formation String:** `Noun + がてら`
- **String Markers:** `がてら`
- **Token Formation Patterns:**
  - [noun] + `がてら`

### Noun こそあれ (~koso are)
**Original Formation String:** `Noun + こそあれ + (result/continuation)`
- **String Markers:** `こそあれ`
- **Token Formation Patterns:**
  - [noun] + `こそあれ`

### Noun こそすれ (~koso sure)
**Original Formation String:** `Noun + こそすれ + (negative or contrasting statement)`
- **String Markers:** `こそすれ`
- **Token Formation Patterns:**
  - [noun] + `こそすれ`

### Noun こそ～が (~koso~ga)
**Original Formation String:** `Noun + こそ + (statement) + が + (contrasting/additional statement)`
- **String Markers:** `こそ`
- **Token Formation Patterns:**
  - [noun] + `こそ` + `が`

### Noun ごとき / Noun ごとく (〜gotoki/〜gotoku)
**Original Formation String:** `Noun + ごとき, Noun + ごとく, Verb-casual + ごとく, い-Adjective + ごとく`
- **String Markers:** `ごとき`, `ごとく`
- **Token Formation Patterns:**
  - [noun] + `ごとき`
  - [noun] + `ごとく`
  - [verb] + `ごとく`
  - [adjective] + `ごとく`

### Noun じゃあるまいし (~ja aru mai shi)
**Original Formation String:** `Noun or Na-Adjective + じゃあるまいし`
- **String Markers:** `じゃあるまいし`
- **Token Formation Patterns:**
  - [noun] + [adjective] + `じゃあるまいし`

### Noun ずくめ (~zukume)
**Original Formation String:** `Noun + ずくめ`
- **String Markers:** `ずくめ`
- **Token Formation Patterns:**
  - [noun] + `ずくめ`

### Noun たりとも～ない (~tari tomo ~nai)
**Original Formation String:** `Noun + たりとも + Negative Verb`
- **String Markers:** `たりとも`
- **Token Formation Patterns:**
  - [noun] + `たりとも` + [verb]

### Noun たる Noun (~taru~)
**Original Formation String:** `Noun1 + たる + Noun2`
- **String Markers:** `たる`
- **Token Formation Patterns:**
  - [noun] + `たる` + [noun]

### Noun だけではすまない (Noun dake dewa sumanai)
**Original Formation String:** `Noun + だけではすまない`
- **String Markers:** `だけではすまない`
- **Token Formation Patterns:**
  - [noun] + `だけではすまない`

### Noun ですら (~desura)
**Original Formation String:** `Noun + ですら`
- **String Markers:** `ですら`
- **Token Formation Patterns:**
  - [noun] + `ですら`

### Noun でなくてなんだろう (〜de nakute nandarou)
**Original Formation String:** `Noun + でなくてなんだろう`
- **String Markers:** `でなくてなんだろう`
- **Token Formation Patterns:**
  - [noun] + `でなくてなんだろう`

### Noun ではあるまいし (~dewa aru maishi)
**Original Formation String:** `Noun + ではあるまいし`
- **String Markers:** `ではあるまいし`
- **Token Formation Patterns:**
  - [noun] + `ではあるまいし`

### Noun と Noun を兼ねて (Noun to Noun o kanete)
**Original Formation String:** `Noun + と + Noun + を兼ねて`
- **String Markers:** `を兼ねて`
- **Token Formation Patterns:**
  - [noun] + `と` + [noun] + `を兼ねて`

### Noun といい Noun といい (〜to ii〜to ii)
**Original Formation String:** `Noun1 + といい + Noun2 + といい + Comment`
- **String Markers:** `といい`
- **Token Formation Patterns:**
  - [noun] + `といい` + [noun] + `といい`

### Noun という Noun (~to iu~)
**Original Formation String:** `Noun1 という Noun2`
- **String Markers:** `という`
- **Token Formation Patterns:**
  - [noun] + `という` + [noun]

### Noun というところだ (Noun to iu tokoro da)
**Original Formation String:** `Noun + というところだ`
- **String Markers:** `というところだ`
- **Token Formation Patterns:**
  - [noun] + `というところだ`

### Noun といったところだ (Noun to itta tokoro da)
**Original Formation String:** `Noun + といったところだ`
- **String Markers:** `といったところだ`
- **Token Formation Patterns:**
  - [noun] + `といったところだ`

### Noun といわず Noun といわず (A to iwazu B to iwazu)
**Original Formation String:** `Noun1 + といわず + Noun2 + といわず + (rest of the sentence)`
- **String Markers:** `といわず`
- **Token Formation Patterns:**
  - [noun] + `といわず` + [noun] + `といわず`

### Noun とは比べものにならない (~to wa kurabemono ni naranai)
**Original Formation String:** `Noun + とは比べものにならない`
- **String Markers:** `とは比べものにならない`
- **Token Formation Patterns:**
  - [noun] + `とは比べものにならない`

### Noun ともなると (〜to mo naru to)
**Original Formation String:** `Noun + ともなると`
- **String Markers:** `ともなると`
- **Token Formation Patterns:**
  - [noun] + `ともなると`

### Noun ともなれば (〜to mo nareba)
**Original Formation String:** `Noun + ともなれば`
- **String Markers:** `ともなれば`
- **Token Formation Patterns:**
  - [noun] + `ともなれば`

### Noun と相まって (~ to aimatte)
**Original Formation String:** `Noun + と相まって`
- **String Markers:** `と相まって`
- **Token Formation Patterns:**
  - [noun] + `と相まって`

### Noun なくして～はない (Noun nakushite ~ wa nai)
**Original Formation String:** `Noun + なくして + Sentence ～はない`
- **String Markers:** `なくして`, `はない`
- **Token Formation Patterns:**
  - [noun] + `なくして` + `はない`

### Noun なしでは～ない (Noun nashi de wa ~nai)
**Original Formation String:** `Noun + なしでは～ない`
- **String Markers:** `なしでは`
- **Token Formation Patterns:**
  - [noun] + `なしでは` + `ない`

### Noun なしには～ない (Noun nashi ni wa ~nai)
**Original Formation String:** `Noun + なしには + Verb-negative`
- **String Markers:** `なしには`
- **Token Formation Patterns:**
  - [noun] + `なしには` + [verb]

### Noun ならいざ知らず (~nara izashirazu)
**Original Formation String:** `Noun1 + ならいざ知らず + Noun2 (comment)`
- **String Markers:** `ならいざ知らず`
- **Token Formation Patterns:**
  - [noun] + `ならいざ知らず` + [noun]

### Noun なり Noun なり (A nari B nari)
**Original Formation String:** `Noun + なり + Noun + なり`
- **String Markers:** `なり`
- **Token Formation Patterns:**
  - [noun] + `なり` + [noun] + `なり`

### Noun なりとも (~nari tomo)
**Original Formation String:** `Noun + なりとも`
- **String Markers:** `なりとも`
- **Token Formation Patterns:**
  - [noun] + `なりとも`

### Noun に Noun を重ねて (A ni B wo kasanete)
**Original Formation String:** `Noun に Noun を重ねて`
- **String Markers:** `を重ねて`
- **Token Formation Patterns:**
  - [noun] + `に` + [noun] + `を重ねて`

### Noun にあっては (Noun ni atte ha)
**Original Formation String:** `Noun + にあっては`
- **String Markers:** `にあっては`
- **Token Formation Patterns:**
  - [noun] + `にあっては`

### Noun にあるまじき Noun (Noun ni aru majiki Noun)
**Original Formation String:** `Noun1 にあるまじき Noun2`
- **String Markers:** `にあるまじき`
- **Token Formation Patterns:**
  - [noun] + `にあるまじき` + [noun]

### Noun にして (Noun ni shite)
**Original Formation String:** `Noun + にして`
- **String Markers:** `にして`
- **Token Formation Patterns:**
  - [noun] + `にして`

### Noun にして初めて (Noun nishite hajimete)
**Original Formation String:** `Noun + にして初めて`
- **String Markers:** `にして初めて`
- **Token Formation Patterns:**
  - [noun] + `にして初めて`

### Noun にすら (〜ni sura)
**Original Formation String:** `Noun + にすら`
- **String Markers:** `にすら`
- **Token Formation Patterns:**
  - [noun] + `にすら`

### Noun にとどまらず～も (~ ni todomarazu ~ mo)
**Original Formation String:** `Noun + にとどまらず + Noun + も`
- **String Markers:** `にとどまらず`
- **Token Formation Patterns:**
  - [noun] + `にとどまらず` + [noun] + `も`

### Noun にひきかえ Noun は (~ni hikikae ~ wa)
**Original Formation String:** `Noun 1 + にひきかえ + Noun 2 + は`
- **String Markers:** `にひきかえ`
- **Token Formation Patterns:**
  - [noun] + `にひきかえ` + [noun] + `は`

### Noun にもまして (〜ni mo mashite)
**Original Formation String:** `Noun + にもまして`
- **String Markers:** `にもまして`
- **Token Formation Patterns:**
  - [noun] + `にもまして`

### Noun によらず (～ni yorazu)
**Original Formation String:** `Noun + によらず`
- **String Markers:** `によらず`
- **Token Formation Patterns:**
  - [noun] + `によらず`

### Noun に先駆けて (〜ni saki gakete)
**Original Formation String:** `Noun + に先駆けて`
- **String Markers:** `に先駆けて`
- **Token Formation Patterns:**
  - [noun] + `に先駆けて`

### Noun に即した Noun (A ni sokushita B)
**Original Formation String:** `Noun1 + に即した + Noun2`
- **String Markers:** `に即した`
- **Token Formation Patterns:**
  - [noun] + `に即した` + [noun]

### Noun に即して Verb (〜ni soku shite ~)
**Original Formation String:** `Noun + に即して + Verb`
- **String Markers:** `に即して`
- **Token Formation Patterns:**
  - [noun] + `に即して` + [verb]

### Noun に言わせれば (Noun ni iwasereba)
**Original Formation String:** `Noun + に言わせれば`
- **String Markers:** `に言わせれば`
- **Token Formation Patterns:**
  - [noun] + `に言わせれば`

### Noun に限ったことではない (〜ni kagitta koto dewa nai)
**Original Formation String:** `Noun + に限ったことではない`
- **String Markers:** `に限ったことではない`
- **Token Formation Patterns:**
  - [noun] + `に限ったことではない`

### Noun に限ったことでもない (~ni kagitta koto demo nai)
**Original Formation String:** `Noun + に限ったことでもない`
- **String Markers:** `に限ったことでもない`
- **Token Formation Patterns:**
  - [noun] + `に限ったことでもない`

### Noun に限る (~ni kagiru)
**Original Formation String:** `Noun + に限る`
- **String Markers:** `に限る`
- **Token Formation Patterns:**
  - [noun] + `に限る`

### Noun ぬいた Noun (A nuita B)
**Original Formation String:** `Noun1 + をぬいた + Noun2`
- **String Markers:** `ぬいた`, `をぬいた`
- **Token Formation Patterns:**
  - [noun] + `をぬいた` + [noun]

### Noun の 嫌いがある (Noun no kirai ga aru)
**Original Formation String:** `Noun + の嫌いがある`
- **String Markers:** `の嫌いがある`
- **Token Formation Patterns:**
  - [noun] + `の嫌いがある`

### Noun の 至り (~no itari)
**Original Formation String:** `Noun + の至り`
- **String Markers:** `の至り`
- **Token Formation Patterns:**
  - [noun] + `の至り`

### Noun のいかんでは (Noun no ikan de wa)
**Original Formation String:** `Noun + のいかんでは`
- **String Markers:** `のいかんでは`
- **Token Formation Patterns:**
  - [noun] + `のいかんでは`

### Noun のいかんにかかわらず (Noun no ikan ni kakawarazu)
**Original Formation String:** `Noun + のいかんにかかわらず`
- **String Markers:** `のいかんにかかわらず`
- **Token Formation Patterns:**
  - [noun] + `のいかんにかかわらず`

### Noun のいかんによっては (Noun no ikan ni yotte wa)
**Original Formation String:** `Noun + のいかんによっては`
- **String Markers:** `のいかんによっては`
- **Token Formation Patterns:**
  - [noun] + `のいかんによっては`

### Noun のいかんによらず (~ no ikan ni yorazu)
**Original Formation String:** `Noun + のいかんによらず`
- **String Markers:** `のいかんによらず`
- **Token Formation Patterns:**
  - [noun] + `のいかんによらず`

### Noun のことだから (〜no koto dakara)
**Original Formation String:** `Noun + のことだから`
- **String Markers:** `のことだから`
- **Token Formation Patterns:**
  - [noun] + `のことだから`

### Noun のごとき Noun (A no gotoki B)
**Original Formation String:** `Noun1 + のごとき + Noun2`
- **String Markers:** `のごとき`
- **Token Formation Patterns:**
  - [noun] + `のごとき` + [noun]

### Noun の手前 (~no temae)
**Original Formation String:** `Noun + の手前`
- **String Markers:** `の手前`
- **Token Formation Patterns:**
  - [noun] + `の手前`

### Noun の極み (〜no kiwami)
**Original Formation String:** `Noun + の極み`
- **String Markers:** `の極み`
- **Token Formation Patterns:**
  - [noun] + `の極み`

### Noun はいざ知らず (~ wa iza shirazu)
**Original Formation String:** `Noun + はいざ知らず, Noun + とは/なんて/しかし etc.`
- **String Markers:** `はいざ知らず`, `とは`, `なんて`, `しかし`
- **Token Formation Patterns:**
  - [noun] + `はいざ知らず`
  - [noun] + `とは` + `なんて` + `しかし`

### Noun はおろか～すら (Noun wa oroka ～sura)
**Original Formation String:** `Noun1 はおろか, Noun2 すら/さえ ～`
- **String Markers:** `はおろか`, `すら`, `さえ`
- **Token Formation Patterns:**
  - [noun] + `はおろか`
  - [noun] + `すら` + `さえ`

### Noun はおろか～まで (~wa oroka ~made)
**Original Formation String:** `Noun1 + はおろか + Noun2 + まで`
- **String Markers:** `はおろか`, `まで`
- **Token Formation Patterns:**
  - [noun] + `はおろか` + [noun] + `まで`

### Noun はおろか～も (Noun wa oroka ～ mo)
**Original Formation String:** `Noun + はおろか + Noun + も`
- **String Markers:** `はおろか`
- **Token Formation Patterns:**
  - [noun] + `はおろか` + [noun] + `も`

### Noun はさておき (~ wa sateoki)
**Original Formation String:** `Noun + はさておき`
- **String Markers:** `はさておき`
- **Token Formation Patterns:**
  - [noun] + `はさておき`

### Noun まみれ (~mamire)
**Original Formation String:** `Noun + まみれ`
- **String Markers:** `まみれ`
- **Token Formation Patterns:**
  - [noun] + `まみれ`

### Noun もさることながら Noun も (A mo saru koto nagara B mo)
**Original Formation String:** `Noun1 + もさることながら + Noun2 + も`
- **String Markers:** `もさることながら`
- **Token Formation Patterns:**
  - [noun] + `もさることながら` + [noun] + `も`

### Noun も兼ねて (~mo kanete)
**Original Formation String:** `Noun + も兼ねて`
- **String Markers:** `も兼ねて`
- **Token Formation Patterns:**
  - [noun] + `も兼ねて`

### Noun も相まって (~mo aimatte)
**Original Formation String:** `Noun + も相まって`
- **String Markers:** `も相まって`
- **Token Formation Patterns:**
  - [noun] + `も相まって`

### Noun を おいて他に Verb ない (〜wo oite hoka ni〜nai)
**Original Formation String:** `Noun + をおいて他に + Verb negative form`
- **String Markers:** `をおいて他に`
- **Token Formation Patterns:**
  - [noun] + `をおいて他に` + [verb]

### Noun をもって (~wo motte)
**Original Formation String:** `Noun + をもって`
- **String Markers:** `をもって`
- **Token Formation Patterns:**
  - [noun] + `をもって`

### Noun をものともせずに (Noun wo mono tomo sezu ni)
**Original Formation String:** `Noun + をものともせずに`
- **String Markers:** `をものともせずに`
- **Token Formation Patterns:**
  - [noun] + `をものともせずに`

### Noun をよそに (~wo yoso ni)
**Original Formation String:** `Noun + をよそに`
- **String Markers:** `をよそに`
- **Token Formation Patterns:**
  - [noun] + `をよそに`

### Noun を余儀なくされる (Noun wo yogi naku sareru)
**Original Formation String:** `Noun + を + 余儀なくされる`
- **String Markers:** `を余儀なくされる`, `余儀なくされる`
- **Token Formation Patterns:**
  - [noun] + `を` + `余儀なくされる`

### Noun を前提として (Noun wo zentei toshite)
**Original Formation String:** `Noun + を前提として`
- **String Markers:** `を前提として`
- **Token Formation Patterns:**
  - [noun] + `を前提として`

### Noun を前提にして (Noun wo zentei ni shite)
**Original Formation String:** `Noun + を前提にして`
- **String Markers:** `を前提にして`
- **Token Formation Patterns:**
  - [noun] + `を前提にして`

### Noun を境にして (Noun wo sakai ni shite)
**Original Formation String:** `Noun + を境に(して)`
- **String Markers:** `を境にして`, `を境に`
- **Token Formation Patterns:**
  - [noun] + `を境に`

### Noun を機にして (~wo ki ni shite)
**Original Formation String:** `Noun + を機にして`
- **String Markers:** `を機にして`
- **Token Formation Patterns:**
  - [noun] + `を機にして`

### Noun を皮切りに / を皮切りにして (Noun wo kawakiri ni / wo kawakiri ni shite)
**Original Formation String:** `Noun + を皮切りに / を皮切りにして`
- **String Markers:** `を皮切りに`, `を皮切りにして`
- **Token Formation Patterns:**
  - [noun] + `を皮切りに` + `を皮切りにして`

### Noun を皮切りにして (Noun wo kawakiri ni shite)
**Original Formation String:** `Noun + を皮切りに (して)`
- **String Markers:** `を皮切りにして`, `を皮切りに`
- **Token Formation Patterns:**
  - [noun] + `を皮切りに`

### Noun を禁じ得ない (〜wo kinjienai)
**Original Formation String:** `Noun + を禁じ得ない`
- **String Markers:** `を禁じ得ない`
- **Token Formation Patterns:**
  - [noun] + `を禁じ得ない`

### Noun を経て (〜wo hete)
**Original Formation String:** `Noun + を経て`
- **String Markers:** `を経て`
- **Token Formation Patterns:**
  - [noun] + `を経て`

### Noun を踏まえて (〜wo fumaete)
**Original Formation String:** `Noun + を踏まえて`
- **String Markers:** `を踏まえて`
- **Token Formation Patterns:**
  - [noun] + `を踏まえて`

### Noun を限りに (Noun wo kagiri ni)
**Original Formation String:** `Noun + を限りに`
- **String Markers:** `を限りに`
- **Token Formation Patterns:**
  - [noun] + `を限りに`

### Noun 並み (~nami)
**Original Formation String:** `Noun + 並み`
- **String Markers:** `並み`
- **Token Formation Patterns:**
  - [noun] + `並み`

### Noun+のいかんだ (Noun no ikan da)
**Original Formation String:** `Noun + のいかんだ/Noun + のいかんでは`
- **String Markers:** `のいかんだ`, `のいかんでは`
- **Token Formation Patterns:**
  - [noun] + `のいかんだ` + [noun] + `のいかんでは`

### Noun1 が Noun1 なら、 Noun2 も Noun2 だ (A ga A nara, B mo B da)
**Original Formation String:** `Noun1 + が + (repeat Noun1) + なら、Noun2 + も + (repeat Noun2) + だ`
- **String Markers:** `なら`
- **Token Formation Patterns:**
  - [noun] + `が` + [noun] + `なら` + [noun] + `も` + [noun] + `だ`

### Noun1 も Noun1 なら、Noun2 も Noun2 だ (A mo A nara, B mo B da)
**Original Formation String:** `Noun1 + も + (repeat Noun1) + なら、Noun2 + も + (repeat Noun2) + だ`
- **String Markers:** `なら`
- **Token Formation Patterns:**
  - [noun] + `も` + [noun] + `なら` + [noun] + `も` + [noun] + `だ`

### Verb がてら (~ gatera)
**Original Formation String:** `Verb (dictionary or -ます stem) + がてら`
- **String Markers:** `がてら`
- **Token Formation Patterns:**
  - [verb] + `がてら`

### Verb こそすれ (~koso sure)
**Original Formation String:** `Verb-ますstem + こそすれ、(絶対に)～ない`
- **String Markers:** `こそすれ`, `絶対に`
- **Token Formation Patterns:**
  - [verb] + `こそすれ` + `ない`

### Verb させられる (~saserareru)
**Original Formation String:** `Verb-casual (non-past) + させられる`
- **String Markers:** `させられる`
- **Token Formation Patterns:**
  - [verb] + `させられる`

### Verb ざるを得ない (~ zaru wo enai)
**Original Formation String:** `Verb-dictionary form + ざるを得ない (する → せざるを得ない)`
- **String Markers:** `ざるを得ない`, `ざるを得ないする`, `せざるを得ない`
- **Token Formation Patterns:**
  - [verb] + `ざるを得ない`

### Verb ずじまい (~zu jimai)
**Original Formation String:** `Verb-ない form (remove ない) + ずじまい`
- **String Markers:** `ずじまい`
- **Token Formation Patterns:**
  - [verb] + `ずじまい`

### Verb ずとも (〜zu tomo)
**Original Formation String:** `Verb-negative stem + ずとも`
- **String Markers:** `ずとも`
- **Token Formation Patterns:**
  - [verb] + `ずとも`

### Verb ずにはおかない (~zuni wa okanai)
**Original Formation String:** `Verb-ない form (remove ない) + ずにはおかない`
- **String Markers:** `ずにはおかない`
- **Token Formation Patterns:**
  - [verb] + `ずにはおかない`

### Verb ずにはすまない (Verb zuni wa sumanai)
**Original Formation String:** `Verb-ない form (remove ない) + ずにはすまない`
- **String Markers:** `ずにはすまない`
- **Token Formation Patterns:**
  - [verb] + `ずにはすまない`

### Verb そうにない (Verb sou ni nai)
**Original Formation String:** `Verb-ますstem + そうにない`
- **String Markers:** `そうにない`
- **Token Formation Patterns:**
  - [verb] + `そうにない`

### Verb そうもない (〜sou mo nai)
**Original Formation String:** `Verb-ますstem + そうもない`
- **String Markers:** `そうもない`
- **Token Formation Patterns:**
  - [verb] + `そうもない`

### Verb そばから (〜soba kara)
**Original Formation String:** `Verb-ますstem + そばから`
- **String Markers:** `そばから`
- **Token Formation Patterns:**
  - [verb] + `そばから`

### Verb たが最後 (〜ta ga saigo)
**Original Formation String:** `Verb-casual, past (た form) + が最後`
- **String Markers:** `たが最後`, `が最後`
- **Token Formation Patterns:**
  - [verb] + `が最後`

### Verb たことにしてください (~ ta koto ni shite kudasai)
**Original Formation String:** `Verb (past, casual) + ことにしてください`
- **String Markers:** `たことにしてください`, `ことにしてください`
- **Token Formation Patterns:**
  - [verb] + `ことにしてください`

### Verb たら Verb たで (~ tara ~ tade)
**Original Formation String:** `Verb-た form + ら + (same Verb-た form) + で`
- **String Markers:** `たら`, `たで`
- **Token Formation Patterns:**
  - [verb] + `ら` + [verb] + `で`

### Verb たら きりがない (Verb tara kiri ga nai)
**Original Formation String:** `Verb-た form + ら + きりがない`
- **String Markers:** `たらきりがない`, `きりがない`
- **Token Formation Patterns:**
  - [verb] + `ら` + `きりがない`

### Verb たら最後 (〜tara saigo)
**Original Formation String:** `Verb-た form + ら最後`
- **String Markers:** `たら最後`, `ら最後`
- **Token Formation Patterns:**
  - [verb] + `ら最後`

### Verb てからというもの (Verb te kara to iu mono)
**Original Formation String:** `Verb-て form + からというもの`
- **String Markers:** `てからというもの`, `からというもの`
- **Token Formation Patterns:**
  - [verb] + `からというもの`

### Verb てこそ (Verb te koso)
**Original Formation String:** `Verb-て form + こそ`
- **String Markers:** `てこそ`, `こそ`
- **Token Formation Patterns:**
  - [verb] + `こそ`

### Verb ては (～te wa)
**Original Formation String:** `Verb-て form + は`
- **String Markers:** `ては`
- **Token Formation Patterns:**
  - [verb] + `は`

### Verb ては Verb (~ te wa ~)
**Original Formation String:** `Verb-て form + は + Verb`
- **String Markers:** `ては`
- **Token Formation Patterns:**
  - [verb] + `は` + [verb]

### Verb てまでも (~ temademo)
**Original Formation String:** `Verb-て form + までも`
- **String Markers:** `てまでも`, `までも`
- **Token Formation Patterns:**
  - [verb] + `までも`

### Verb てみせる (Verb te miseru)
**Original Formation String:** `Verb-て form + みせる`
- **String Markers:** `てみせる`, `みせる`
- **Token Formation Patterns:**
  - [verb] + `みせる`

### Verb てやまない (Verb te yamanai)
**Original Formation String:** `Verb-て form + やまない (common with certain verbs)`
- **String Markers:** `てやまない`, `やまない`
- **Token Formation Patterns:**
  - [verb] + `やまない`

### Verb ないではおかない (~ nai de wa okanai)
**Original Formation String:** `Verb-ない form + ではおかない`
- **String Markers:** `ないではおかない`, `ではおかない`
- **Token Formation Patterns:**
  - [verb] + `ではおかない`

### Verb ないではすまない (Verb nai dewa sumanai)
**Original Formation String:** `Verb-ない form + ではすまない`
- **String Markers:** `ないではすまない`, `ではすまない`
- **Token Formation Patterns:**
  - [verb] + `ではすまない`

### Verb ないまでも (Verb nai made mo)
**Original Formation String:** `Verb-ない form + までも`
- **String Markers:** `ないまでも`, `までも`
- **Token Formation Patterns:**
  - [verb] + `までも`

### Verb ないものだろうか (Verb nai mono darou ka)
**Original Formation String:** `Verb-negative (often negative potential) + ものだろうか`
- **String Markers:** `ないものだろうか`, `ものだろうか`
- **Token Formation Patterns:**
  - [verb] + `ものだろうか`

### Verb ないものでもない (Verb nai mono demo nai)
**Original Formation String:** `Verb-negative form (ない form) + ものでもない`
- **String Markers:** `ないものでもない`, `ものでもない`
- **Token Formation Patterns:**
  - [verb] + `ものでもない`

### Verb の ない Noun (~ no nai ~)
**Original Formation String:** `Verb in negative form + の + Noun`
- **String Markers:** `のない`
- **Token Formation Patterns:**
  - [verb] + `の` + [noun]

### Verb ば きりがない (〜ba kiri ga nai)
**Original Formation String:** `Verb-conditional form (ば) + きりがない`
- **String Markers:** `ばきりがない`, `きりがない`
- **Token Formation Patterns:**
  - [verb] + `きりがない`

### Verb もしないで (~ mo shinai de)
**Original Formation String:** `Verb (masu stem) + もしないで`
- **String Markers:** `もしないで`
- **Token Formation Patterns:**
  - [verb] + `もしないで`

### Verb やしない (~ yashinai)
**Original Formation String:** `Verb (masu stem) + やしない`
- **String Markers:** `やしない`
- **Token Formation Patterns:**
  - [verb] + `やしない`

### Verb よう (~ you / ~ you ni)
**Original Formation String:** `Verb (dictionary or negative form) + ように (する / etc.)`
- **String Markers:** `よう`, `ようにする`, `ように`
- **Token Formation Patterns:**
  - [verb] + `ように`

### Verb ようか Verbるまいか (Verb you ka Verb ru mai ka)
**Original Formation String:** `Verb-volitional form + か + Verb-volitional negative form (まい) + か`
- **String Markers:** `ようか`, `るまいか`, `まい`
- **Token Formation Patterns:**
  - [verb] + `か` + [verb] + `か`

### Verb ようが Verb るまいが (Verb you ga Verb ru mai ga)
**Original Formation String:** `Verb-volitional form + が + Verb-negative volitional form + が`
- **String Markers:** `ようが`, `るまいが`
- **Token Formation Patterns:**
  - [verb] + `が` + [verb] + `が`

### Verb ようがない (〜you ga nai)
**Original Formation String:** `Verb (masu stem) + ようがない`
- **String Markers:** `ようがない`
- **Token Formation Patterns:**
  - [verb] + `ようがない`

### Verb ようと Verbる まいと (Verb you to Verb ru mai to)
**Original Formation String:** `Verb-volitional + と + Verb-negative volitional (～まい) + と`
- **String Markers:** `ようと`, `るまいと`, `まい`
- **Token Formation Patterns:**
  - [verb] + `と` + [verb] + `と`

### Verb ようにも (〜you ni mo)
**Original Formation String:** `Verb-volitional form + にも + (reason/potential negative, etc.)`
- **String Markers:** `ようにも`, `にも`
- **Token Formation Patterns:**
  - [verb] + `にも`

### Verb ようにも Verb れない (〜you ni mo 〜renai)
**Original Formation String:** `Verb-volitional form + にも + (potential negative form / reason)`
- **String Markers:** `ようにも`, `れない`, `にも`
- **Token Formation Patterns:**
  - [verb] + `にも`

### Verb ようもない (~you mo nai)
**Original Formation String:** `Verb-ます stem + ようもない`
- **String Markers:** `ようもない`
- **Token Formation Patterns:**
  - [verb] + `ようもない`

### Verbる / Noun(である) + 限り(は) (kagiri (wa))
**Original Formation String:** `Verb-dictionary form + 限り(は)
Noun(である) + 限り(は)`
- **String Markers:** `である`, `限りは`, `限り`
- **Token Formation Patterns:**
  - [verb] + `限り` + [noun] + `限り`

### Verbる がままに (〜ga mama ni)
**Original Formation String:** `Verb-dictionary form + がままに`
- **String Markers:** `るがままに`, `がままに`
- **Token Formation Patterns:**
  - [verb] + `がままに`

### Verbる が早いか (verb-ru ga hayai ka)
**Original Formation String:** `Verb-dictionary form + が早いか`
- **String Markers:** `るが早いか`, `が早いか`
- **Token Formation Patterns:**
  - [verb] + `が早いか`

### Verbる くらいなら (〜ru kurai nara)
**Original Formation String:** `Verb-dictionary form + くらいなら`
- **String Markers:** `るくらいなら`, `くらいなら`
- **Token Formation Patterns:**
  - [verb] + `くらいなら`

### Verbる こと なし に (Verb-ru koto nashi ni)
**Original Formation String:** `Verb-dictionary form + ことなしに`
- **String Markers:** `ることなしに`, `ことなしに`
- **Token Formation Patterns:**
  - [verb] + `ことなしに`

### Verbる ことのないように (Verb-ru koto no nai you ni)
**Original Formation String:** `Verb-dictionary form + ことのないように`
- **String Markers:** `ることのないように`, `ことのないように`
- **Token Formation Patterns:**
  - [verb] + `ことのないように`

### Verbる ときりがない (verb-ru to kiri ga nai)
**Original Formation String:** `Verb-casual + と + きりがない`
- **String Markers:** `るときりがない`, `きりがない`
- **Token Formation Patterns:**
  - [verb] + `と` + `きりがない`

### Verbる ともなく Verb (Verb-ru tomonaku Verb)
**Original Formation String:** `Verb-dictionary form + ともなく + Verb`
- **String Markers:** `るともなく`, `ともなく`
- **Token Formation Patterns:**
  - [verb] + `ともなく` + [verb]

### Verbる ともなしに Verb (Verb-ru tomonashi ni Verb)
**Original Formation String:** `Verb-dictionary form + ともなしに + Verb`
- **String Markers:** `るともなしに`, `ともなしに`
- **Token Formation Patterns:**
  - [verb] + `ともなしに` + [verb]

### Verbる なり (Verb-ru nari)
**Original Formation String:** `Verb-dictionary form + なり`
- **String Markers:** `るなり`, `なり`
- **Token Formation Patterns:**
  - [verb] + `なり`

### Verbる にとどまらず～も (Verb-ru ni todomarazu ~ mo)
**Original Formation String:** `Noun / Verb-dictionary form + にとどまらず + も/ほかのこと`
- **String Markers:** `るにとどまらず`, `にとどまらず`, `ほかのこと`
- **Token Formation Patterns:**
  - [noun] + [verb] + `にとどまらず` + `も` + `ほかのこと`

### Verbる にはあたらない (Verb-ru ni wa ataranai)
**Original Formation String:** `Verb-dictionary form + にはあたらない`
- **String Markers:** `るにはあたらない`, `にはあたらない`
- **Token Formation Patterns:**
  - [verb] + `にはあたらない`

### Verbる にも (Verb-ru ni mo)
**Original Formation String:** `Verb-dictionary form + にも + (reason it can't be done)`
- **String Markers:** `るにも`, `にも`
- **Token Formation Patterns:**
  - [verb] + `にも`

### Verbる にも Verb れない (Verb-ru ni mo Verb-re nai)
**Original Formation String:** `Verb-volitional + にも + Verb-potential negative`
- **String Markers:** `るにも`, `れない`, `にも`
- **Token Formation Patterns:**
  - [verb] + `にも` + [verb]

### Verbる べからざる Noun (Verb-ru bekara zaru Noun)
**Original Formation String:** `Verb-dictionary form + べからざる + Noun`
- **String Markers:** `るべからざる`, `べからざる`
- **Token Formation Patterns:**
  - [verb] + `べからざる` + [noun]

### Verbる べからず (〜ru bekara zu)
**Original Formation String:** `Verb-ru + べからず`
- **String Markers:** `るべからず`, `べからず`
- **Token Formation Patterns:**
  - [verb] + `べからず`

### Verbる べく (Verb-ru beku)
**Original Formation String:** `Verb-dictionary form + べく`
- **String Markers:** `るべく`, `べく`
- **Token Formation Patterns:**
  - [verb] + `べく`

### Verbる べくもない (Verb-ru beku mo nai)
**Original Formation String:** `Verb-dictionary form + べくもない`
- **String Markers:** `るべくもない`, `べくもない`
- **Token Formation Patterns:**
  - [verb] + `べくもない`

### Verbる までもない (〜ru made mo nai)
**Original Formation String:** `Verb-る + までもない`
- **String Markers:** `るまでもない`, `までもない`
- **Token Formation Patterns:**
  - [verb] + `までもない`

### Verbる ものとする (〜ru mono to suru)
**Original Formation String:** `Verb-dictionary form + ものとする`
- **String Markers:** `るものとする`, `ものとする`
- **Token Formation Patterns:**
  - [verb] + `ものとする`

### Verbる や否や (Verb-ru ya ina ya)
**Original Formation String:** `Verb-dictionary form + や否や`
- **String Markers:** `るや否や`, `や否や`
- **Token Formation Patterns:**
  - [verb] + `や否や`

### Verbる 始末だ (〜ru shimatsu da)
**Original Formation String:** `Verb-dictionary form + 始末だ`
- **String Markers:** `る始末だ`, `始末だ`
- **Token Formation Patterns:**
  - [verb] + `始末だ`

### Verbる 嫌いがある (～ru kirai ga aru)
**Original Formation String:** `Verb-dictionary form + 嫌いがある`
- **String Markers:** `る嫌いがある`, `嫌いがある`
- **Token Formation Patterns:**
  - [verb] + `嫌いがある`

### いつまで～のやら (itsumade ~ no yara)
**Original Formation String:** `いつまで + Verb (dictionary form) + のやら`
- **String Markers:** `いつまで`, `のやら`
- **Token Formation Patterns:**
  - `いつまで` + [verb] + `のやら`

### どんなに～うが (donna ni ～ u ga)
**Original Formation String:** `どんなに + Verb-volitional + うが, どんなに + い-Adjective(～かろう) + が, どんなに + な-Adjective + だろうが`
- **String Markers:** `どんなに`, `うが`, `かろう`, `だろうが`
- **Token Formation Patterns:**
  - `どんなに` + [verb] + `うが` + `どんなに` + [adjective] + `が` + `どんなに` + [adjective] + `だろうが`

### ～かと思いきや (〜ka to omoikiya)
**Original Formation String:** `Sentence + かと思いきや (Verb plain form, i-/na-Adjective, or Noun + だ + かと思いきや)`
- **String Markers:** `かと思いきや`
- **Token Formation Patterns:**
  - `かと思いきや` + [verb] + [adjective] + [noun] + `だ` + `かと思いきや`

### ～から Noun に 至る まで (〜kara 〜ni itaru made)
**Original Formation String:** `Noun (start) + から + Noun (end) + に至るまで`
- **String Markers:** `から`, `に至るまで`
- **Token Formation Patterns:**
  - [noun] + `から` + [noun] + `に至るまで`

### ～が Verb られる (〜ga Verb rareru)
**Original Formation String:** `❶ (Group 1) Verb:  書く → 書ける / 飲む → 飲める, etc.
❷ (Group 2) Verb-ます stem + られる (食べる→食べられる、見る→見られる)`
- **String Markers:** `られる`, `書く`, `書ける`, `飲む`
- **Token Formation Patterns:**
  - [verb] + `書く` + `書ける` + `飲む` + `飲める` + [verb] + `られる`

### ～がゆえに (～ga yue ni)
**Original Formation String:** `Noun / Verb / Adjective + がゆえに`
- **String Markers:** `がゆえに`
- **Token Formation Patterns:**
  - [noun] + [verb] + [adjective] + `がゆえに`

### ～がゆえの Noun (〜ga yue no Noun)
**Original Formation String:** `Noun / Verb-dictionary form + がゆえの + Noun`
- **String Markers:** `がゆえの`
- **Token Formation Patterns:**
  - [noun] + [verb] + `がゆえの` + [noun]

### ～こととて (〜koto tote)
**Original Formation String:** `Verb (plain form) + こととて / Noun + の + こととて / (な-Adjective + な) + こととて`
- **String Markers:** `こととて`
- **Token Formation Patterns:**
  - [verb] + `こととて` + [noun] + `の` + `こととて` + [adjective] + `な` + `こととて`

### ～ごとく (〜gotoku)
**Original Formation String:** `Verb-て + ごとく / Noun + の + ごとく`
- **String Markers:** `ごとく`
- **Token Formation Patterns:**
  - [verb] + `ごとく` + [noun] + `の` + `ごとく`

### ～ずにすんだ (〜zuni sunda)
**Original Formation String:** `Verb-ず form + に + すんだ`
- **String Markers:** `ずにすんだ`, `すんだ`
- **Token Formation Patterns:**
  - [verb] + `に` + `すんだ`

### ～だろうとなかろうと (〜darou to nakarou to)
**Original Formation String:** `Noun / i-Adjective / na-Adjective / Verb + だろうとなかろうと`
- **String Markers:** `だろうとなかろうと`
- **Token Formation Patterns:**
  - [noun] + [adjective] + [adjective] + [verb] + `だろうとなかろうと`

### ～つもりだ (〜tsumori da)
**Original Formation String:** `Verb-dictionary form + つもりだ`
- **String Markers:** `つもりだ`
- **Token Formation Patterns:**
  - [verb] + `つもりだ`

### ～つもりで (〜tsumori de)
**Original Formation String:** `Verb-dictionary form + つもりで`
- **String Markers:** `つもりで`
- **Token Formation Patterns:**
  - [verb] + `つもりで`

### ～ではすまない (〜dewa sumanai)
**Original Formation String:** `Verb-dictionary form + ではすまない / い-Adjective + ではすまない / な-Adjective + ではすまない / Noun + ではすまない`
- **String Markers:** `ではすまない`
- **Token Formation Patterns:**
  - [verb] + `ではすまない` + [adjective] + `ではすまない` + [adjective] + `ではすまない` + [noun] + `ではすまない`

### ～とあって (〜to atte)
**Original Formation String:** `Noun + とあって / (Sometimes Verb + とあって, depending on context)`
- **String Markers:** `とあって`
- **Token Formation Patterns:**
  - [noun] + `とあって` + [verb] + `とあって`

### ～とあれば (〜to areba)
**Original Formation String:** `Verb-casual + とあれば / い-Adjective + とあれば / な-Adjective + だとあれば / Noun + だとあれば`
- **String Markers:** `とあれば`, `だとあれば`
- **Token Formation Patterns:**
  - [verb] + `とあれば` + [adjective] + `とあれば` + [adjective] + `だとあれば` + [noun] + `だとあれば`

### ～といえども (〜to iedomo)
**Original Formation String:** `Noun + といえども / Verb-plain form + といえども / Adjective + といえども`
- **String Markers:** `といえども`
- **Token Formation Patterns:**
  - [noun] + `といえども` + [verb] + `といえども` + [adjective] + `といえども`

### ～といったらありはしない (〜to ittara ari wa shinai)
**Original Formation String:** `Noun + といったらありはしない / な-Adjective + といったらありはしない`
- **String Markers:** `といったらありはしない`
- **Token Formation Patterns:**
  - [noun] + `といったらありはしない` + [adjective] + `といったらありはしない`

### ～といったらありゃしない (〜to ittara arya shinai)
**Original Formation String:** `Verb-casual + といったらありゃしない / い-Adjective + といったらありゃしない / な-Adjective + だ + といったらありゃしない / Noun + だ + といったらありゃしない`
- **String Markers:** `といったらありゃしない`
- **Token Formation Patterns:**
  - [verb] + `といったらありゃしない` + [adjective] + `といったらありゃしない` + [adjective] + `だ` + `といったらありゃしない` + [noun] + `だ` + `といったらありゃしない`

### ～といったらない (〜to ittara nai)
**Original Formation String:** `い-Adjective + といったらない / な-Adjective + だといったらない / Noun + だといったらない`
- **String Markers:** `といったらない`, `だといったらない`
- **Token Formation Patterns:**
  - [adjective] + `といったらない` + [adjective] + `だといったらない` + [noun] + `だといったらない`

### ～ときている (〜to kite iru)
**Original Formation String:** `Verb-casual / い-Adjective / な-Adjective（＋だ） / Noun（＋だ） + ときている`
- **String Markers:** `ときている`
- **Token Formation Patterns:**
  - [verb] + [adjective] + [adjective] + [noun] + `ときている`

### ～ところを (〜tokoro wo)
**Original Formation String:** `Verb-ている + ところを / Noun + の + ところを / い-Adjective + ところを / な-Adjective + な + ところを`
- **String Markers:** `ところを`, `ている`
- **Token Formation Patterns:**
  - [verb] + `ところを` + [noun] + `の` + `ところを` + [adjective] + `ところを` + [adjective] + `な` + `ところを`

### ～とされる (〜to sareru)
**Original Formation String:** `Verb-casual + とされる / い-Adjective + とされる / な-Adjective + だとされる / Noun + だとされる`
- **String Markers:** `とされる`, `だとされる`
- **Token Formation Patterns:**
  - [verb] + `とされる` + [adjective] + `とされる` + [adjective] + `だとされる` + [noun] + `だとされる`

### ～としたところで (〜to shita tokoro de)
**Original Formation String:** `Verb-casual + としたところで / い-Adjective + としたところで / な-Adjective + だとしたところで / Noun + だとしたところで`
- **String Markers:** `としたところで`, `だとしたところで`
- **Token Formation Patterns:**
  - [verb] + `としたところで` + [adjective] + `としたところで` + [adjective] + `だとしたところで` + [noun] + `だとしたところで`

### ～とすると (〜to suru to)
**Original Formation String:** `Verb-casual + とすると / い-Adjective + とすると / な-Adjective + だとすると / Noun + だとすると`
- **String Markers:** `とすると`, `だとすると`
- **Token Formation Patterns:**
  - [verb] + `とすると` + [adjective] + `とすると` + [adjective] + `だとすると` + [noun] + `だとすると`

### ～とすれば (～to sureba)
**Original Formation String:** `Verb-casual + とすれば / い-Adjective + とすれば / な-Adjective + だとすれば / Noun + だとすれば`
- **String Markers:** `とすれば`, `だとすれば`
- **Token Formation Patterns:**
  - [verb] + `とすれば` + [adjective] + `とすれば` + [adjective] + `だとすれば` + [noun] + `だとすれば`

### ～となったら (〜to nattara)
**Original Formation String:** `Verb-casual + となったら / Noun + となったら`
- **String Markers:** `となったら`
- **Token Formation Patterns:**
  - [verb] + `となったら` + [noun] + `となったら`

### ～となると (〜to naru to)
**Original Formation String:** `Verb-casual + となると / い-Adjective + となると / な-Adjective + だとなると / Noun + だとなると`
- **String Markers:** `となると`, `だとなると`
- **Token Formation Patterns:**
  - [verb] + `となると` + [adjective] + `となると` + [adjective] + `だとなると` + [noun] + `だとなると`

### ～となれば (〜to nareba)
**Original Formation String:** `Verb-casual + となれば, い-Adjective + となれば, な-Adjective + だとなれば, Noun + だとなれば`
- **String Markers:** `となれば`, `だとなれば`
- **Token Formation Patterns:**
  - [verb] + `となれば`
  - [adjective] + `となれば`
  - [adjective] + `だとなれば`
  - [noun] + `だとなれば`

### ～とのことだ (〜to no koto da)
**Original Formation String:** `Simplified phrase + とのことだ`
- **String Markers:** `とのことだ`
- **Token Formation Patterns:** *None successfully parsed*

### ～とはいえ (～to wa ie)
**Original Formation String:** `Noun + とはいえ, な-Adjective + だとはいえ, い-Adjective + とはいえ, Verb-casual + とはいえ`
- **String Markers:** `とはいえ`, `だとはいえ`
- **Token Formation Patterns:**
  - [noun] + `とはいえ`
  - [adjective] + `だとはいえ`
  - [adjective] + `とはいえ`
  - [verb] + `とはいえ`

### ～とみえて (〜to miete)
**Original Formation String:** `Verb-casual + とみえて, い-Adjective + とみえて, な-Adjective + だとみえて, Noun + だとみえて`
- **String Markers:** `とみえて`, `だとみえて`
- **Token Formation Patterns:**
  - [verb] + `とみえて`
  - [adjective] + `とみえて`
  - [adjective] + `だとみえて`
  - [noun] + `だとみえて`

### ～とみられる (～to mirareru)
**Original Formation String:** `Verb-casual + とみられる, Noun + とみられる`
- **String Markers:** `とみられる`
- **Token Formation Patterns:**
  - [verb] + `とみられる`
  - [noun] + `とみられる`

### ～とみると (〜to miru to)
**Original Formation String:** `Verb-casual + とみると, い-Adjective + とみると, な-Adjective + だとみると, Noun + だとみると`
- **String Markers:** `とみると`, `だとみると`
- **Token Formation Patterns:**
  - [verb] + `とみると`
  - [adjective] + `とみると`
  - [adjective] + `だとみると`
  - [noun] + `だとみると`

### ～と言わんばかりに (〜to iwan bakari ni)
**Original Formation String:** `Verb-volitional + と言わんばかりに, い-Adjective + と言わんばかりに, な-Adjective + だと言わんばかりに, Noun + だと言わんばかりに`
- **String Markers:** `と言わんばかりに`, `だと言わんばかりに`
- **Token Formation Patterns:**
  - [verb] + `と言わんばかりに`
  - [adjective] + `と言わんばかりに`
  - [adjective] + `だと言わんばかりに`
  - [noun] + `だと言わんばかりに`

### ～と言わんばかりの Noun (～to iwan bakari no Noun)
**Original Formation String:** `Verb-plain form + と言わんばかりの Noun`
- **String Markers:** `と言わんばかりの`
- **Token Formation Patterns:**
  - [verb] + `と言わんばかりの` + [noun]

### ～ながらに (～nagara ni)
**Original Formation String:** `Common set phrases: 生まれながらに, 涙ながらに, 昔ながらに, 子供ながらに, etc.`
- **String Markers:** `ながらに`, `生まれながらに`, `涙ながらに`, `昔ながらに`
- **Token Formation Patterns:** *None successfully parsed*

### ～ながらの Noun (〜nagara no Noun)
**Original Formation String:** `Verb-ますstem (or plain minus る) + ながら + の + Noun`
- **String Markers:** `ながらの`, `ながら`
- **Token Formation Patterns:**
  - [verb] + `ながら` + `の` + [noun]

### ～ながらも (〜nagara mo)
**Original Formation String:** `Verb stem + ながらも, い-Adjective + ながらも, な-Adjective/Noun + ながらも`
- **String Markers:** `ながらも`
- **Token Formation Patterns:**
  - [verb] + `ながらも`
  - [adjective] + `ながらも`
  - [adjective] + [noun] + `ながらも`

### ～なくはない (〜naku wa nai)
**Original Formation String:** `Verb-ないform + なくはない, い-Adjective－い + くはない, な-Adjective + ではなくはない, Noun + ではなくはない`
- **String Markers:** `なくはない`, `くはない`, `ではなくはない`
- **Token Formation Patterns:**
  - [verb] + `なくはない`
  - [adjective] + `い` + `くはない`
  - [adjective] + `ではなくはない`
  - [noun] + `ではなくはない`

### ～なくもない (〜naku mo nai)
**Original Formation String:** `Verb-ないform + なくもない, い-Adjective－い + くもない, な-Adjective + でもない, Noun + でもない`
- **String Markers:** `なくもない`, `くもない`, `でもない`
- **Token Formation Patterns:**
  - [verb] + `なくもない`
  - [adjective] + `い` + `くもない`
  - [adjective] + `でもない`
  - [noun] + `でもない`

### ～なら～なりに
**Original Formation String:** `Noun/Adjective + なら + (same Noun/Adjective) + なりに`
- **String Markers:** `なら`, `なりに`
- **Token Formation Patterns:**
  - [noun] + [adjective] + `なら` + [noun] + [adjective] + `なりに`

### ～には及ばない (〜ni wa oyobanai)
**Original Formation String:** `Verb-dictionary form + には及ばない`
- **String Markers:** `には及ばない`
- **Token Formation Patterns:**
  - [verb] + `には及ばない`

### ～に堪えない (～ni taenai)
**Original Formation String:** `Verb-dictionary form + に堪えない, Noun + に堪えない`
- **String Markers:** `に堪えない`
- **Token Formation Patterns:**
  - [verb] + `に堪えない`
  - [noun] + `に堪えない`

### ～に堪える (～ni taeru)
**Original Formation String:** `Verb-dictionary form + に堪える, Noun + に堪える`
- **String Markers:** `に堪える`
- **Token Formation Patterns:**
  - [verb] + `に堪える`
  - [noun] + `に堪える`

### ～に耐える (～ni taeru)
**Original Formation String:** `Noun + に耐える`
- **String Markers:** `に耐える`
- **Token Formation Patterns:**
  - [noun] + `に耐える`

### ～に至った (〜ni itatta)
**Original Formation String:** `Verb-てform + に至った or Noun / Verb-dictionary + に至る (more general).`
- **String Markers:** `に至った`, `に至る`
- **Token Formation Patterns:**
  - [verb] + `に至った` + [noun] + [verb] + `に至る`

### ～に越したことはない (〜ni koshita koto wa nai)
**Original Formation String:** `Verb (dictionary form) + に越したことはない, い-Adjective + に越したことはない, な-Adjective/Noun + である + に越したことはない`
- **String Markers:** `に越したことはない`, `である`
- **Token Formation Patterns:**
  - [verb] + `に越したことはない`
  - [adjective] + `に越したことはない`
  - [adjective] + [noun] + `である` + `に越したことはない`

### ～に難くない (～ni katakunai)
**Original Formation String:** `Verb-dictionary form + に難くない (commonly with 想像する, 理解する, 察する, etc.)`
- **String Markers:** `に難くない`, `想像する`, `理解する`, `察する`
- **Token Formation Patterns:**
  - [verb] + `に難くない`

### ～ぬく (~nuku)
**Original Formation String:** `Verb-stem + ぬく`
- **String Markers:** `ぬく`
- **Token Formation Patterns:**
  - [verb] + `ぬく`

### ～のは Noun ぐらいのものだ (〜no wa Noun gurai no mono da)
**Original Formation String:** `Verb-casual + のは + Noun + ぐらいのものだ, い-Adjective + のは + Noun + ぐらいのものだ, etc.`
- **String Markers:** `のは`, `ぐらいのものだ`
- **Token Formation Patterns:**
  - [verb] + `のは` + [noun] + `ぐらいのものだ`
  - [adjective] + `のは` + [noun] + `ぐらいのものだ`

### ～ば～ものを (～ba～mono o)
**Original Formation String:** `Verb-ば + Verb-past + ものを, い-Adjective + ければ + ものを, な-Adjective/Noun + であれば + ものを, etc.`
- **String Markers:** `ものを`, `ければ`, `であれば`
- **Token Formation Patterns:**
  - [verb] + [verb] + `ものを`
  - [adjective] + `ければ` + `ものを`
  - [adjective] + [noun] + `であれば` + `ものを`

### ～びた (～bita)
**Original Formation String:** `[Noun/Adjective stem] + びた (forms a 連体形 modifier, e.g., 大人びた人 “an adult-like person”)`
- **String Markers:** `びた`, `連体形`, `大人びた人`
- **Token Formation Patterns:** *None successfully parsed*

### ～びる (〜biru)
**Original Formation String:** `Adjective/Noun + びる (to form a verb)`
- **String Markers:** `びる`
- **Token Formation Patterns:**
  - [adjective] + [noun] + `びる`

### ～ぶった (～butta)
**Original Formation String:** `Noun/Adjective + ぶる → ぶった (past tense), e.g., 偉そうぶった, 大人ぶった`
- **String Markers:** `ぶった`, `ぶる`, `偉そうぶった`, `大人ぶった`
- **Token Formation Patterns:**
  - [noun] + [adjective] + `ぶる` + `ぶった` + `偉そうぶった` + `大人ぶった`

### ～ぶって (〜butte)
**Original Formation String:** `Noun/Adjective + ぶる → ぶって (te-form)`
- **String Markers:** `ぶって`, `ぶる`
- **Token Formation Patterns:**
  - [noun] + [adjective] + `ぶる` + `ぶって`

### ～ぶり (〜buri)
**Original Formation String:** `Time expression + ぶり`
- **String Markers:** `ぶり`
- **Token Formation Patterns:** *None successfully parsed*

### ～ぶる (〜buru)
**Original Formation String:** `Noun / (Adjective stem) + ぶる`
- **String Markers:** `ぶる`
- **Token Formation Patterns:**
  - [noun] + [adjective] + `ぶる`

### ～までだ (～made da)
**Original Formation String:** `Verb (dictionary/ない form) + までだ, い-Adjective + までだ, Noun + までだ`
- **String Markers:** `までだ`
- **Token Formation Patterns:**
  - [verb] + `までだ`
  - [adjective] + `までだ`
  - [noun] + `までだ`

### ～もなんでもない (〜mo nandemonai)
**Original Formation String:** `Verb-dictionary form + もなんでもない, い-Adjective + もなんでもない, な-Adjective + なもなんでもない, Noun + もなんでもない`
- **String Markers:** `もなんでもない`, `なもなんでもない`
- **Token Formation Patterns:**
  - [verb] + `もなんでもない`
  - [adjective] + `もなんでもない`
  - [adjective] + `なもなんでもない`
  - [noun] + `もなんでもない`

### ～ものとして (～mono to shite)
**Original Formation String:** `Verb-casual + ものとして, い-Adjective + ものとして, な-Adjective + なものとして, Noun + のものとして`
- **String Markers:** `ものとして`, `なものとして`, `のものとして`
- **Token Formation Patterns:**
  - [verb] + `ものとして`
  - [adjective] + `ものとして`
  - [adjective] + `なものとして`
  - [noun] + `のものとして`

### ～んがために (〜n ga tame ni)
**Original Formation String:** `Verb-negative stem + んがために`
- **String Markers:** `んがために`
- **Token Formation Patterns:**
  - [verb] + `んがために`

### ～んばかりに (〜n bakari ni)
**Original Formation String:** `Verb-negative stem + ん + ばかりに`
- **String Markers:** `んばかりに`, `ばかりに`
- **Token Formation Patterns:**
  - [verb] + `ん` + `ばかりに`

### ～差し支えない (〜sashitsukaenai)
**Original Formation String:** `Verb-て form + も差し支えない, Noun + が差し支えない`
- **String Markers:** `差し支えない`, `も差し支えない`, `が差し支えない`
- **Token Formation Patterns:**
  - [verb] + `も差し支えない`
  - [noun] + `が差し支えない`

### ～折に (〜ori ni)
**Original Formation String:** `Verb-dictionary form + 折に, Verb-た形 + 折に, Noun + の折に`
- **String Markers:** `折に`, `た形`, `の折に`
- **Token Formation Patterns:**
  - [verb] + `折に`
  - [verb] + `折に`
  - [noun] + `の折に`

### ～極まりない (〜kiwamarinai)
**Original Formation String:** `な-Adjective（語幹）+ 極まりない, い-Adjective（連用形）+ こと + 極まりない, Noun + の極まりない`
- **String Markers:** `極まりない`, `語幹`, `連用形`, `こと`
- **Token Formation Patterns:**
  - [adjective] + `極まりない`
  - [adjective] + `こと` + `極まりない`
  - [noun] + `の極まりない`

### ～極まる (〜kiwamaru)
**Original Formation String:** `な-Adjective（語幹）+ 極まる, い-Adjective（連用形）+ こと + 極まる, etc.`
- **String Markers:** `極まる`, `語幹`, `連用形`, `こと`
- **Token Formation Patterns:**
  - [adjective] + `極まる`
  - [adjective] + `こと` + `極まる`

### ～足りない (～tarinai)
**Original Formation String:** `Noun + (が) 足りない, Verb-casual + ほど/だけ + (が) 足りない`
- **String Markers:** `足りない`, `が足りない`, `ほど`, `だけ`
- **Token Formation Patterns:**
  - [noun] + `足りない`
  - [verb] + `ほど` + `だけ` + `足りない`

### ～足る Noun (〜taru Noun)
**Original Formation String:** `Noun/Verb-dictionary form + に足る + Noun`
- **String Markers:** `足る`, `に足る`
- **Token Formation Patterns:**
  - [noun] + [verb] + `に足る` + [noun]

### ～限りだ (〜kagiri da)
**Original Formation String:** `い-Adjective + 限りだ, な-Adjective + な/である + 限りだ, Noun + の + 限りだ`
- **String Markers:** `限りだ`, `である`
- **Token Formation Patterns:**
  - [adjective] + `限りだ`
  - [adjective] + `な` + `である` + `限りだ`
  - [noun] + `の` + `限りだ`
