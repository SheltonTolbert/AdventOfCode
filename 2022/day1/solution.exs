defmodule Solution do
  def sum([]) do
    0
  end

  def sum([h | t]) do
    h + sum(t)
  end

  def parseInt(string) do
    {num, _} = Integer.parse(string)
    num
  end

  def parse_input({:ok, input}) do
    stream =
      input
      |> String.split("\n")
      |> Stream.map(fn x -> if x == "", do: "-1", else: x end)
      |> Stream.map(&parseInt(&1))
      |> Stream.chunk_by(&(&1 == -1))
      |> Stream.map(&sum(&1))

    Enum.max(stream)
  end

  def solve(input_file) do
    parse_input(File.read(input_file))
  end
end
