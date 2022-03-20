myMap = {
  "a": {
    "b": { "cost": 6 },
    "d": { "cost": 4 },
    "g": { "cost": 18 }
  },
  "b": {
    "a": { "cost": 6 },
    "c": { "cost": 5 },
    "e": { "cost": 4 },
    "h": { "cost": 6 }
  },
  "d": {
    "a": { "cost": 4 },
    "c": { "cost": 15 },
  },
  "c": {
    "d": { "cost": 15 },
    "b": { "cost": 5 },
    "f": { "cost": 8 },
  },
  "f": {
    "c": { "cost": 8 },
    "e": { "cost": 7 },
    "g": { "cost": 3 }
  },
  "e": {
    "f": { "cost": 7 },
    "g": { "cost": 5 },
  },
  "g": {
    "f": { "cost": 3 },
    "e": { "cost": 5 },
    "h": { "cost": 6 },
  },
   "h": {
    "b": { "cost": 6 },
    "g": { "cost": 6 },
  }
}

heuristic = {
  "a": 18,
  "b": 9,
  "c": 11,
  "d": 23,
  "e": 5,
  "f": 3,
  "g": 0,
  "h": 6,
}