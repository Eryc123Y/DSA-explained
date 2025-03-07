#import "@preview/dvdtyp:1.0.1": *
#import "../typesetting.typ": *
#import "@preview/mitex:0.2.5": *
#import "@preview/codly:1.2.0": *
#import "@preview/codedis:0.1.0": *
#import "@preview/wrap-it:0.1.1": *
#import "@preview/codly-languages:0.1.8": *
#import "@preview/cetz:0.3.3"
#import "@preview/cetz-plot:0.1.1"
#import "@preview/equate:0.3.1": *
#import "@preview/quick-maths:0.2.1": *
#import "@preview/lovelace:0.3.0": *

#show: shorthands.with(
  ($+-$, $plus.minus$),
  ($|-$, math.tack),
)

#show: equate.with(breakable: true, sub-numbering: true)

#show: dvdtyp.with(
  title: "Preliminary Concepts of Algorithm and Data Structure",
  subtitle: [],
  author: "Xingyu Yang",
  abstract: "",
)
#show: codly-init

#codly(
  languages: (
    py: (
      name: "Python",
      icon: "🐍",
      color: rgb("#3572A5")
    )
  )
)


#outline()
#pagebreak()