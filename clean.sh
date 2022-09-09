#!/usr/bin/env bash


del()
{
  \rm log.lammps || true
  \rm *.txt || true
}

main()
{
  del
}


main "${@}"

