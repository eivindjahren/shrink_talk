# Help, I need to download 1gb of data to reproduce the bug!
---


TODO

* Demo app and data
  * data as csv, loaded into dataframe
  * Demoapp
     * Throw divide by zero inside of map(lambda a,b: df[a] / df[b], zip(columns1, columns2))
     * replace 0 by 1 in all columns but secretly flip it back if a columned is named 'bozo'
     * Maybe hide the bug in an inherited classes property.
  * Talk about experience with SAT solvers.
