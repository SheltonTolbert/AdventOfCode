defmodule Solution do
  def solve do
    "Error: Provide the path to the input file"
  end

  def parse_range(input) do
    [start, stop] = String.split(input, "-")
    String.to_integer(start)..String.to_integer(stop)
  end

  def is_subset?(range1, range2) do
    Enum.all?(range1, fn x -> Enum.member?(range2, x) end)
  end

  def reduce([left, right], x) do
    if is_subset?(parse_range(left), parse_range(right)) ||
         is_subset?(parse_range(right), parse_range(left)) do
      x + 1
    else
      x + 0
    end
  end

  def reduce([""], acc) do
    acc
  end

  def solve({:ok, input}) do
    input
    |> String.split("\n")
    |> Enum.map(fn x -> String.split(x, ",") end)
    |> Enum.reduce(0, &reduce(&1, &2))
  end

  def solve(input_file) do
    solve(File.read(input_file))
  end
end
