export function randData(params = "key for properties") {
    return fetch(`/randData?params=${params}`)
      .then((r) => r.json())
      .then((data) => {
        return data
      })
  }
  