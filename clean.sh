#!/usr/bin/env bash


del()
{
  \rm log.lammps || true
  \rm *.txt  || true
  \rm aa.dat || true
  \rm *.traj || true
}

main()
{
  del
}


main "${@}"

